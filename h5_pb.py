#-*- coding:utf-8 -*-
import os
import numpy as np
import tensorflow as tf
from keras.models import Model
from keras import backend as K
from model import efficientnet_B4
from tensorflow.python.platform import gfile
import cv2
import pdb

def h5_to_pb(h5_model, output_dir, model_name, out_prefix = "output_", log_tensorboard = False):
    K.set_learning_phase(0)
    out_nodes = []

    for i in range(len(h5_model.outputs)):
        out_nodes.append(out_prefix + str(i + 1))
        tf.identity(h5_model.outputs[i], out_prefix + str(i + 1))
    sess = K.get_session()

    from tensorflow.python.framework import graph_util,graph_io

    init_graph = sess.graph.as_graph_def()
    main_graph = graph_util.convert_variables_to_constants(sess, init_graph, out_nodes)
    graph_io.write_graph(main_graph, output_dir, name = model_name, as_text = False)

    if log_tensorboard:
        from tensorflow.python.tools import import_pb_to_tensorboard
        import_pb_to_tensorboard.import_to_tensorboard(osp.join(output_dir, model_name), output_dir)

if __name__ == '__main__':
    #hdf5 model convert to pb model
    model = efficientnet_B4()
    model_path = 'checkpoints/weights.005-1.185-0.95325.hdf5'
    model.load_weights(model_path)
    print('load model over!')
    basemodel = Model(inputs = model.input, outputs = model.get_layer('dense_1').output)
    h5_to_pb(basemodel, output_dir='pb_model', model_name='model_imagededup.pb')
    print('pb model has saved sucessfully!')
