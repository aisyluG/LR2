# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sendedBox = QtWidgets.QGroupBox(self.centralwidget)
        self.sendedBox.setGeometry(QtCore.QRect(0, 0, 250, 355))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.sendedBox.setFont(font)
        self.sendedBox.setObjectName("sendedBox")
        self.sendBt = QtWidgets.QPushButton(self.sendedBox)
        self.sendBt.setGeometry(QtCore.QRect(12, 310, 231, 28))
        self.sendBt.setObjectName("sendBt")
        self.sendedText = QtWidgets.QTextEdit(self.sendedBox)
        self.sendedText.setGeometry(QtCore.QRect(0, 20, 250, 271))
        self.sendedText.setReadOnly(True)
        self.sendedText.setObjectName("sendedText")
        self.gettedBox = QtWidgets.QGroupBox(self.centralwidget)
        self.gettedBox.setGeometry(QtCore.QRect(270, 0, 250, 355))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.gettedBox.setFont(font)
        self.gettedBox.setObjectName("gettedBox")
        self.gettedText = QtWidgets.QTextEdit(self.gettedBox)
        self.gettedText.setGeometry(QtCore.QRect(0, 20, 250, 271))
        self.gettedText.setReadOnly(True)
        self.gettedText.setObjectName("gettedText")
        self.threadNumberSBox = QtWidgets.QSpinBox(self.gettedBox)
        self.threadNumberSBox.setGeometry(QtCore.QRect(30, 310, 71, 22))
        self.threadNumberSBox.setMinimum(1)
        self.threadNumberSBox.setObjectName("threadNumberSBox")
        self.okBt = QtWidgets.QPushButton(self.gettedBox)
        self.okBt.setGeometry(QtCore.QRect(130, 310, 101, 28))
        self.okBt.setObjectName("okBt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Producer-Customer"))
        self.sendedBox.setTitle(_translate("MainWindow", "Отправленные сообщения"))
        self.sendBt.setText(_translate("MainWindow", "Отправить сообщение"))
        self.gettedBox.setTitle(_translate("MainWindow", "Полученные сообщения"))
        self.okBt.setText(_translate("MainWindow", "OK"))
