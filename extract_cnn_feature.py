# -*- coding: utf-8 -*-
'''
extract features using CNN
'''
import os
import numpy as np
import re
import cv2
import pdb
import tensorflow as tf
from keras import backend as K
from tensorflow.python.platform import gfile
from sklearn.preprocessing import Binarizer
from collections import Counter
from numpy import linalg as LA


class Extract_featuresCNN:
    def __init__(self):
        self.pb_path = 'pb_model/model_imagededup_new.pb'
        self.sess = tf.Session()
        init = tf.global_variables_initializer()
        self.sess.run(init)
        with tf.gfile.FastGFile(self.pb_path, "rb") as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            self.sess.graph.as_default()
            tf.import_graph_def(graph_def, name="")

        self.inputs = self.sess.graph.get_tensor_by_name('input_1:0')
        self.outputs = self.sess.graph.get_tensor_by_name('dense_1/Tanh:0')

        self.ones_np = np.array([Counter(bin(i).replace('0b', ''))['1'] for i in range(65536)])

    '''
    extract image feature vector
    '''
    def extract_feat(self, img):
        feat = self.sess.run(self.outputs, feed_dict={self.inputs: img})
        return feat[0]

    '''
    crop text region function using mask
    '''
    def crop_text(self, img, threshold):
        ret, image_mask = cv2.threshold(img, threshold, 1, cv2.THRESH_BINARY_INV)
        n = np.argwhere(image_mask == 1)
        rows = np.unique([n[i][0] for i in range(n.shape[0])])
        cols = np.unique([n[i][1] for i in range(n.shape[0])])
        min_row = np.min(rows)
        max_row = np.max(rows)
        min_col = np.min(cols)
        max_col = np.max(cols)
        image_crop = img[min_row: max_row, min_col: max_col]
        return image_crop
    
	
    def convert_bin(self, feat):
        feat_bin = Binarizer(threshold=0.0).fit(feat.reshape(-1, 1))
        feat_bin = feat_bin.transform(feat.reshape(-1, 1)).squeeze()
        feat_bin = ''.join([bin(int(i)).replace('0b', '') for i in list(feat_bin)])

        # binary/16bit---->int
        feat_bin = re.findall(r'.{16}', feat_bin)
        feat_int = np.array([int(i, base=2) for i in feat_bin])
        return feat_int

    '''
    Use densenet model to extract features
    Output: normalized feature vector
    '''
    # extract cnn feature
    def dense_extract_bin(self, img_path):
        img = cv2.imread(img_path, 0)
        h, w = img.shape[:2]
        img_l = img[:, : int(w / 2)]
        img_r = img[:, -int(w / 2):]
        
        # crop text rgion
		# img = self.crop_text(img, 120)

        img_l = cv2.resize(img_l, (380, 380), interpolation=cv2.INTER_LINEAR)[:, :, np.newaxis]
        img_r = cv2.resize(img_r, (380, 380), interpolation=cv2.INTER_LINEAR)[:, :, np.newaxis]
        img_l = 1. - img_l / 255.
        img_r = 1. - img_r / 255.
        img_l = np.expand_dims(img_l, axis=0)
        img_r = np.expand_dims(img_r, axis=0)
        feat_l = self.extract_feat(img_l) # (1024, )
        feat_r = self.extract_feat(img_r) # (1024, )
        feat = np.concatenate((feat_l, feat_r)) #(2048, )

        # binary process
        feat_int = self.convert_bin(feat) #(64, )

        # add num_ones
        num_ones = np.sum(self.ones_np[feat_int], axis=0)
        feat = np.concatenate((feat_int, num_ones[np.newaxis, ]))
        return feat


    def dense_extract_ori(self, img_path):
        img = cv2.imread(img_path, 0)
        #img = self.crop_text(img, 120)
        img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_LINEAR)[:, :, np.newaxis]
        img = 1. - img / 255.0
        img = np.expand_dims(img, axis=0)
        feat = self.extract_feat(img) # (2048, )
        norm_feat = feat / LA.norm(feat)
        return norm_feat

