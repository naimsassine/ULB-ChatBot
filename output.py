# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(585, 567)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 300, 211))
        self.label.setMaximumSize(QtCore.QSize(300, 300))
        self.label.setStyleSheet("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.netID = QtWidgets.QTextEdit(self.centralwidget)
        self.netID.setGeometry(QtCore.QRect(220, 350, 131, 31))
        self.netID.setAutoFillBackground(False)
        self.netID.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.netID.setObjectName("netID")
        self.signInButton = QtWidgets.QPushButton(self.centralwidget)
        self.signInButton.setGeometry(QtCore.QRect(210, 470, 151, 51))
        self.signInButton.setObjectName("signInButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 400, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 350, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 400, 81, 31))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">Welcome</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Welcome to SAL!</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">The ULB\'s first ChatBot!</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Ready to ask some questions?</span></p></body></html>"))
        self.netID.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.signInButton.setText(_translate("MainWindow", "Let\'s Go!"))
        self.label_2.setText(_translate("MainWindow", "         NetID : "))
        self.label_3.setText(_translate("MainWindow", "    Password : "))
