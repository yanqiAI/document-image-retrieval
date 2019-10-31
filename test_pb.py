#-*- coding:utf-8 -*-
import os
import numpy as np
from keras.layers import Input
from keras.models import Model
import tensorflow as tf
from keras import backend as K
from keras.models import load_model
from densenet_model import densenet
from tensorflow.python.platform import gfile
import cv2
import pdb

def load_pb(img, pb_path=None):
    sess = tf.Session()
    init = tf.global_variables_initializer()
    sess.run(init)
    with tf.gfile.FastGFile(pb_path,"rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        sess.graph.as_default()

        for node in graph_def.node:
            if node.op == 'RefSwitch':
                node.op = 'Switch'
                for index in range(len(node.input)):
                    if 'moving_' in node.input[index]:
                        node.input[index] = node.input[index] + '/read'
            elif node.op == 'AssignSub':
                node.op = 'Sub'
                if 'use_locking' in node.attr:
                    del node.attr['use_locking']

        tf.import_graph_def(graph_def,name="")

    inputs = sess.graph.get_tensor_by_name('input_2:0')
    outputs = sess.graph.get_tensor_by_name('dense_1/Tanh:0')
    #outputs = sess.graph.get_tensor_by_name('lambda_1/l2_normalize:0')
    out = sess.run(outputs, feed_dict={inputs: img}).squeeze()
    return out

if __name__ == '__main__':
    img = cv2.imread('111.jpg', 0)
    img = cv2.resize(img, (380,  380), interpolation=cv2.INTER_LINEAR)[:, :, np.newaxis]
    img = 1.0 - np.array(img).astype(np.float32) / 255.0
    img = np.expand_dims(img, 0)
    feat_pb = load_pb(img, pb_path = "./pb_model/model_efficinet4_snn.pb")
    print('pb_feat:', feat_pb)
