# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'retrieval.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1740, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(400, 20, 391, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.scrollArea1 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea1.setGeometry(QtCore.QRect(10, 80, 371, 101))
        self.scrollArea1.setFont(font)
        self.scrollArea1.setWidgetResizable(True)
        self.scrollArea1.setObjectName("scrollArea1")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 369, 99))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea1.setWidget(self.scrollAreaWidgetContents)

        self.scrollArea6 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea6.setGeometry(QtCore.QRect(390, 110, 1311, 741))
        self.scrollArea6.setFont(font)
        self.scrollArea6.setWidgetResizable(True)
        self.scrollArea6.setObjectName("scrollArea6")

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1310, 740))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea6.setWidget(self.scrollAreaWidgetContents_2)

        # self.scrollArea2 = QtWidgets.QScrollArea(self.centralwidget)
        # self.scrollArea2.setGeometry(QtCore.QRect(390, 60, 1311, 121))
        # self.scrollArea2.setFont(font)
        # self.scrollArea2.setWidgetResizable(True)
        # self.scrollArea2.setObjectName("scrollArea2")
        #
        # self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 1311, 741))
        # self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        # self.scrollArea2.setWidget(self.scrollAreaWidgetContents_5)

        self.labelpixel1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.labelpixel1.setGeometry(QtCore.QRect(0, 0, 650, 365))
        self.labelpixel1.setText("")
        self.labelpixel1.setObjectName("labelpixel1")

        self.labelpixel2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.labelpixel2.setGeometry(QtCore.QRect(655, 0, 650, 365))
        self.labelpixel2.setText("")
        self.labelpixel2.setObjectName("labelpixel2")

        self.labelpixel3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.labelpixel3.setGeometry(QtCore.QRect(0, 370, 650, 365))
        self.labelpixel3.setText("")
        self.labelpixel3.setObjectName("labelpixel3")

        self.labelpixel4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.labelpixel4.setGeometry(QtCore.QRect(655, 370, 650, 365))
        self.labelpixel4.setText("")
        self.labelpixel4.setObjectName("labelpixel4")

        # self.labelpixel5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        # self.labelpixel5.setGeometry(QtCore.QRect(10, 410, 650, 360))
        # self.labelpixel5.setText("")
        # self.labelpixel5.setObjectName("labelpixel5")

        # self.labelpixel6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        # self.labelpixel6.setGeometry(QtCore.QRect(10, 530, 650, 360))
        # self.labelpixel6.setText("")
        # self.labelpixel6.setObjectName("labelpixel6")


        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(400, 70, 111, 31))
        self.label2.setFont(font)
        self.label2.setObjectName("label2")

        self.scrollArea3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea3.setGeometry(QtCore.QRect(10, 240, 371, 171))
        self.scrollArea3.setFont(font)
        self.scrollArea3.setWidgetResizable(True)
        self.scrollArea3.setObjectName("scrollArea3")

        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 369, 169))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.pushButton3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton3.setGeometry(QtCore.QRect(200, 10, 151, 41))
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName("pushButton3")

        self.radioButton1 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_3)
        self.radioButton1.setGeometry(QtCore.QRect(40, 20, 121, 31))
        self.radioButton1.setFont(font)
        self.radioButton1.setObjectName("radioButton1")

        self.pushButton4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton4.setGeometry(QtCore.QRect(200, 90, 151, 41))
        self.pushButton4.setFont(font)
        self.pushButton4.setObjectName("pushButton4")

        self.radioButton2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_3)
        self.radioButton2.setGeometry(QtCore.QRect(40, 90, 141, 31))
        self.radioButton2.setFont(font)
        self.radioButton2.setObjectName("radioButton2")

        self.labelfeat1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.labelfeat1.setGeometry(QtCore.QRect(210, 55, 151, 21))
        self.labelfeat1.setText("")
        self.labelfeat1.setObjectName("labelfeat1")
        self.labelfeat2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.labelfeat2.setGeometry(QtCore.QRect(210, 140, 151, 21))
        self.labelfeat2.setText("")
        self.labelfeat2.setObjectName("labelfeat2")
        self.scrollArea3.setWidget(self.scrollAreaWidgetContents_3)
        self.scrollArea6 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea6.setGeometry(QtCore.QRect(10, 640, 371, 211))
        self.scrollArea6.setFont(font)
        self.scrollArea6.setWidgetResizable(True)
        self.scrollArea6.setObjectName("scrollArea6")

        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 369, 209))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_4)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 371, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.scrollArea6.setWidget(self.scrollAreaWidgetContents_4)
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(10, 610, 131, 21))
        self.label3.setFont(font)
        self.label3.setObjectName("label3")

        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_4)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 371, 211))
        font_text = QtGui.QFont()
        font_text.setFamily("黑体")
        font_text.setPointSize(13)
        self.textBrowser.setFont(font_text)
        self.textBrowser.setObjectName("textBrowser")

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(210, 20, 171, 31))
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")

        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(10, 20, 191, 31))
        self.lineEdit1.setFont(font)
        self.lineEdit1.setObjectName("lineEdit1")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(210, 120, 171, 31))
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")

        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(20, 120, 181, 31))
        self.lineEdit2.setFont(font)
        self.lineEdit2.setObjectName("lineEdit2")

        self.scrollArea4_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea4_2.setGeometry(QtCore.QRect(10, 430, 371, 141))
        self.scrollArea4_2.setWidgetResizable(True)
        self.scrollArea4_2.setObjectName("scrollArea4_2")

        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 369, 139))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")

        self.pushButton5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton5.setGeometry(QtCore.QRect(50, 20, 201, 41))
        self.pushButton5.setFont(font)
        self.pushButton5.setObjectName("pushButton5")

        self.labelmodel = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.labelmodel.setGeometry(QtCore.QRect(263, 29, 101, 21))
        self.labelmodel.setObjectName("labelmodel")
        self.scrollArea4_2.setWidget(self.scrollAreaWidgetContents_6)

        self.pushButton6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton6.setGeometry(QtCore.QRect(50, 80, 201, 41))
        self.pushButton6.setFont(font)
        self.pushButton6.setObjectName("pushButton6")
        self.scrollArea4_2.setWidget(self.scrollAreaWidgetContents_6)

        self.labelquery = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.labelquery.setGeometry(QtCore.QRect(263, 89, 101, 21))
        self.labelquery.setObjectName("labelquery")
        self.scrollArea4_2.setWidget(self.scrollAreaWidgetContents_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1429, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #增加一个进度条
        self.pbar = QtWidgets.QProgressBar(self.scrollAreaWidgetContents_3)
        self.pbar.setGeometry(QtCore.QRect(10, 135, 201, 21))
        self.pbar.setVisible(False)
        self.timer = QtCore.QBasicTimer() #创建一个计时器
        self.re_extraction = True  # 是否重复提取特征

        self.retranslateUi(MainWindow)
        self.pushButton1.clicked.connect(self.bnt1_click)
        self.pushButton2.clicked.connect(self.bnt2_click)
        self.pushButton3.clicked.connect(self.bnt3_click)
        self.pushButton4.clicked.connect(self.bnt4_click)
        self.pushButton5.clicked.connect(self.bnt5_click)
        self.pushButton6.clicked.connect(self.bnt6_click)

        self.radioButton1.setChecked(True) #默认被选中，表示特征文件已经存在
        self.radioButton1.toggled.connect(self.on_radiobutton1_toggled) #连接一个按钮是否被激活的响应函数
        self.radioButton2.toggled.connect(self.on_radiobutton2_toggled)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "七天教育扫描试卷检索系统"))
        self.label1.setText(_translate("MainWindow", "当前选择的图像库中一共有****张图片"))
        self.label2.setText(_translate("MainWindow", "检索结果top3"))
        self.pushButton3.setText(_translate("MainWindow", "导入特征库文件"))
        self.radioButton1.setText(_translate("MainWindow", "已有特征库"))
        self.pushButton4.setText(_translate("MainWindow", "提取图像库特征"))
        self.radioButton2.setText(_translate("MainWindow", "建立新的特征库"))
        self.label3.setText(_translate("MainWindow", "检索结果反馈"))
        self.pushButton1.setText(_translate("MainWindow", "选择图像库"))
        self.pushButton2.setText(_translate("MainWindow", "选择待检索文件"))
        self.pushButton5.setText(_translate("MainWindow", "加载模型"))
        self.pushButton6.setText(_translate("MainWindow", "开始检索"))

