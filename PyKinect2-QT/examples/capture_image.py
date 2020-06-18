# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'capture_image.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import QVideoWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 10, 661, 531))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.start_toolButton = QtWidgets.QToolButton(self.frame)
        self.start_toolButton.setGeometry(QtCore.QRect(50, 110, 161, 51))
        self.start_toolButton.setObjectName("start_toolButton")
        self.stop_toolButton = QtWidgets.QToolButton(self.frame)
        self.stop_toolButton.setGeometry(QtCore.QRect(430, 110, 161, 51))
        self.stop_toolButton.setObjectName("stop_toolButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 40, 101, 41))
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.image_line = QtWidgets.QLineEdit(self.frame)
        self.image_line.setGeometry(QtCore.QRect(230, 50, 61, 21))
        self.image_line.setText("")
        self.image_line.setObjectName("image_line")
        self.color_widget = QtWidgets.QWidget(self.frame)
        self.color_widget.setGeometry(QtCore.QRect(30, 220, 261, 281))
        self.color_widget.setObjectName("color_widget")
        self.color_widget = QVideoWidget(self.color_widget)
        self.depth_widget = QtWidgets.QWidget(self.frame)
        self.color_widget.setGeometry(QtCore.QRect(30, 220, 261, 281))
        self.depth_widget.setGeometry(QtCore.QRect(380, 220, 261, 281))
        self.depth_widget.setObjectName("depth_widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # self.start_toolButton.clicked.connect(MainWindow.close)
        # self.stop_toolButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "kinect采集程序"))
        self.start_toolButton.setText(_translate("MainWindow", "开始采集"))
        self.stop_toolButton.setText(_translate("MainWindow", "保存视频"))
        self.label.setText(_translate("MainWindow", "采集图像数量："))

