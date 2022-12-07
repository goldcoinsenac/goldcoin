# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GoldCoinsTelaVitoria.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from GoldCoins import Ui_TelaInicial


class Ui_TelaVitoria(object):
    def OpenMainWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TelaInicial()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, TelaVitoria):
        TelaVitoria.setObjectName("TelaVitoria")
        TelaVitoria.resize(1005, 694)
        self.centralwidget = QtWidgets.QWidget(TelaVitoria)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QtWidgets.QFrame(self.centralwidget)
        self.top.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top.setStyleSheet("background-color: #fff;")
        self.top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top.setObjectName("top")
        self.verticalLayout.addWidget(self.top)
        self.containerlogo = QtWidgets.QFrame(self.centralwidget)
        self.containerlogo.setMaximumSize(QtCore.QSize(16777215, 80))
        self.containerlogo.setStyleSheet("background-color: #fff;")
        self.containerlogo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.containerlogo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.containerlogo.setObjectName("containerlogo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.containerlogo)
        self.verticalLayout_2.setContentsMargins(30, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo = QtWidgets.QFrame(self.containerlogo)
        self.logo.setMaximumSize(QtCore.QSize(281, 61))
        self.logo.setStyleSheet("background-image: url(:/Logo/Icone GoldCoins pqn.png);\n"
"background-repeat: norepeat;")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.verticalLayout_2.addWidget(self.logo)
        self.verticalLayout.addWidget(self.containerlogo)
        self.container = QtWidgets.QFrame(self.centralwidget)
        self.container.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.container.setStyleSheet("background-color: #fff;")
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.container)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.container_2 = QtWidgets.QFrame(self.container)
        self.container_2.setMaximumSize(QtCore.QSize(450, 650))
        self.container_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.container_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container_2.setObjectName("container_2")
        self.label = QtWidgets.QLabel(self.container_2)
        self.label.setGeometry(QtCore.QRect(124, 40, 201, 61))
        self.label.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(251, 190, 119);\n"
"font-weight: bold;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.container_2)
        self.label_2.setGeometry(QtCore.QRect(15, 210, 421, 31))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(72, 63, 51);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.container_2)
        self.label_3.setGeometry(QtCore.QRect(135, 160, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(251, 190, 119);")
        self.label_3.setObjectName("label_3")
        self.SignInButton = QtWidgets.QPushButton(self.container_2, clicked = lambda: self.OpenMainWindow())
        self.SignInButton.setGeometry(QtCore.QRect(135, 330, 161, 51))
        self.SignInButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SignInButton.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    background-color: #81BAFD;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #738FF0;\n"
"}\n"
"")
        self.SignInButton.setObjectName("SignInButton")
        self.horizontalLayout.addWidget(self.container_2)
        self.verticalLayout.addWidget(self.container)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bottom.setStyleSheet("background-color: #fff;")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.label_4 = QtWidgets.QLabel(self.bottom)
        self.label_4.setGeometry(QtCore.QRect(820, 10, 178, 18))
        self.label_4.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(251, 190, 119);\n"
"font-weight: bold;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.bottom)
        TelaVitoria.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaVitoria)
        QtCore.QMetaObject.connectSlotsByName(TelaVitoria)

    def retranslateUi(self, TelaVitoria):
        _translate = QtCore.QCoreApplication.translate
        TelaVitoria.setWindowTitle(_translate("TelaVitoria", "GoldCoins"))
        self.label.setText(_translate("TelaVitoria", "Parabéns!"))
        self.label_2.setText(_translate("TelaVitoria", "Prossiga para a etapa de cadastro."))
        self.label_3.setText(_translate("TelaVitoria", "Você ganhou!"))
        self.SignInButton.setText(_translate("TelaVitoria", "Prosseguir!"))
        self.label_4.setText(_translate("TelaVitoria", "2022 CopyRight © Solutech"))
#import images_rc
