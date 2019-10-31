# coding:utf-8
import sys
import os
import random
import numpy as np
import cv2
import time
import h5py
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui_retrieval import *

from extract_cnn_feature import Extract_featuresCNN
from collections import Counter
from numpy import linalg as LA
from IPython.core.debugger import Tracer

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

    def bnt1_click(self):
        self.files_path = QFileDialog.getExistingDirectory(self, "选择要查询的数据库")
        self.lineEdit1.setText(self.files_path)
        self.files_list = os.listdir(self.files_path)

        # dataset information
        files_num = len(self.files_list)
        self.label1.setText('数据库文件统计信息：数据库中一共有{}张图像'.format(files_num))

    def bnt2_click(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, "选择要查询的图像", './test_images', '*.png *.jpg *.bmp')
        self.lineEdit2.setText(self.filename)

        # show image
        jpg = QtGui.QPixmap(self.filename, '1').scaled(self.labelpixel1.size(), QtCore.Qt.KeepAspectRatio)
        self.labelpixel1.setPixmap(jpg)

    def on_radiobutton1_toggled(self):
        self.radioButton1 = self.sender()
        if self.radioButton1.isChecked():
            print("Feats file has existed")

    def on_radiobutton2_toggled(self):
        self.radioButton2 = self.sender()
        if self.radioButton2.isChecked():
            print("Start to extract images feats")

    def bnt3_click(self):
        if self.radioButton1.isChecked():
            self.index_path = QFileDialog.getOpenFileName(self, "选择数据库特征文件", "./cnn_feature", "*.npz")
            if self.index_path[0] != '' and self.index_path[1] == '*.npz':
                self.labelfeat1.setText("特征文件导入成功")
            else:
                self.labelfeat1.setText("特征文件导入失败")
        else:
            self.labelfeat1.setText("特征文件不存在")

    def bnt4_click(self):
        if not self.radioButton2.isChecked():
            self.labelfeat2.setText("特征文件已经存在")

        elif self.re_extraction == True:
            feats = []
            names = []
            step = 0
            model = Extract_featuresCNN()
            self.pbar.setVisible(True)
            ones_np = np.array([Counter(bin(i).replace('0b', ''))['1'] for i in range(65536)])
            start_time = time.time()
            for i, img_path in enumerate(self.files_list):
                if i >= len(self.files_list):
                    self.timer.stop()
                else:
                    img_path = self.files_path + '/' + img_path
                    img_name = os.path.split(img_path)[1]
                    feat_int = model.dense_extract_bin(img_path) #(65, )

                    feats.append(feat_int)
                    names.append(img_name)

                    step = step + 1
                    step_ = int(100 * (step / len(self.files_list)))
                    self.pbar.setValue(step_)
                    if step % 100 == 0:
                        print('{} processed successfully!'.format(step))

            index_path = 'cnn_feature'
            feats_name = 'Dense_featureCNN_database_1w_chemistry_1024'
            np.savez_compressed(index_path + '/' + feats_name, feats = feats, names = names)

            end_time = time.time()
            cost_time = end_time - start_time
            self.labelfeat2.setText('提取完成！用时{}s'.format(str(round(cost_time, 1))))
            self.index_path = (index_path + '/' + feats_name + '.npz', '*.npz')
            self.re_extraction = False
        else:
            self.labelfeat2.setText("特征文件已经存在！")


    def bnt5_click(self):
        # load model and extract queryVec
        self.model = Extract_featuresCNN()
        self.labelmodel.setText("模型加载成功")


    def bnt6_click(self):
        if self.index_path[0] != '':
            # load npz file
            featureCNN_path = self.index_path[0]
            npz_file = np.load(featureCNN_path)
            self.feats = npz_file['feats']
            self.names = npz_file['names']
            self.feats_score = self.feats[:, -1:].squeeze() / 2048 #(num, )

            ones_np = np.array([Counter(bin(i).replace('0b', ''))['1'] for i in range(65536)])

            queryVec = self.model.dense_extract_bin(self.filename) #(65, )
            queryVec_score = queryVec[-1:] / 2048
			
            # create the candidate dataset
            query_range = np.where((np.abs(self.feats_score - queryVec_score) < 0.15))

            feats_search = self.feats[query_range][:, :-1] #(num, 64)
            names_search = self.names[query_range]

            start_time = time.time()
            k = 5

            dists_search = np.sum(ones_np[np.bitwise_xor(queryVec[:-1, ], [feat for feat in feats_search])], axis=1)
            topK_index = np.argpartition(dists_search, k)[:k]
            topK_index_order = topK_index[np.argsort(dists_search[topK_index])]
            rank_score = 1. - dists_search[topK_index_order] / np.max(dists_search)
            imglist = names_search[topK_index_order]

            end_time = time.time()
            cost_time = end_time - start_time
            self.labelquery.setText('用时{}s '.format(str(round(cost_time, 5))))

            # show rearch results
            # top_1 = QtGui.QPixmap(self.files_path + '/' + imglist[0], "1").scaled(self.labelpixel2.size(), QtCore.Qt.KeepAspectRatio)
            # self.labelpixel2.setPixmap(top_1)

            top_2 = QtGui.QPixmap(self.files_path + '/' + imglist[1], "1").scaled(self.labelpixel2.size(), QtCore.Qt.KeepAspectRatio)
            self.labelpixel2.setPixmap(top_2)

            top_3 = QtGui.QPixmap(self.files_path + '/' + imglist[2], "1").scaled(self.labelpixel3.size(), QtCore.Qt.KeepAspectRatio)
            self.labelpixel3.setPixmap(top_3)

            top_4 = QtGui.QPixmap(self.files_path + '/' + imglist[3], "1").scaled(self.labelpixel4.size(), QtCore.Qt.KeepAspectRatio)
            self.labelpixel4.setPixmap(top_4)

            # top_5 = QtGui.QPixmap(self.files_path + '/' + imglist[4], "1").scaled(self.labelpixel6.size(), QtCore.Qt.KeepAspectRatio)
            # self.labelpixel6.setPixmap(top_5)

            self.textBrowser.setText(
                '本次查询相似度最高的{}张图片依次为：\n top1:{}, score:{}\n top2:{}, score:{}\n top3:{}, score:{}\n top4:{}, score:{}\n top5:{}, score:{}'
                    .format(str(k), imglist[0].split('-')[-1], '%.3f' % rank_score[0], imglist[1].split('-')[-1], '%.3f' % rank_score[1],
                                    imglist[2].split('-')[-1], '%.3f' % rank_score[2], imglist[3].split('-')[-1], '%.3f' % rank_score[3],
                                    imglist[4].split('-')[-1], '%.3f' % rank_score[4]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
