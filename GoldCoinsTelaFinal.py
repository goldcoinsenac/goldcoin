from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaFinal(object):
    def setupUi(self, TelaFinal):
        TelaFinal.setObjectName("TelaFinal")
        TelaFinal.resize(1005, 694)
        self.centralwidget = QtWidgets.QWidget(TelaFinal)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QtWidgets.QFrame(self.centralwidget)
        self.top.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top.setStyleSheet("background-color: rgb(251, 190, 119);")
        self.top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top.setObjectName("top")
        self.verticalLayout.addWidget(self.top)
        self.container = QtWidgets.QFrame(self.centralwidget)
        self.container.setStyleSheet("background-color: rgb(251, 190, 119);")
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.container)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.container)
        self.frame.setMaximumSize(QtCore.QSize(700, 900))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(200, 20, 291, 201))
        self.frame_2.setMaximumSize(QtCore.QSize(291, 201))
        self.frame_2.setStyleSheet("background-image: url(:/Logo/IconeGoldCoins.png);\n"
"background-repeat: norepeat;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(240, 310, 211, 51))
        self.label_4.setMaximumSize(QtCore.QSize(211, 51))
        self.label_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(72, 63, 51);\n"
"font-weight: bold;")
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(80, 370, 521, 81))
        self.textBrowser.setMaximumSize(QtCore.QSize(521, 81))
        self.textBrowser.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(72, 63, 51);\n"
"font-weight: bold;\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(260, 500, 161, 51))
        self.label_5.setMaximumSize(QtCore.QSize(161, 51))
        self.label_5.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(251, 190, 119);\n"
"font-weight: bold;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout.addWidget(self.container)
        self.bot = QtWidgets.QFrame(self.centralwidget)
        self.bot.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bot.setStyleSheet("background-color: rgb(251, 190, 119);")
        self.bot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bot.setObjectName("bot")
        self.label_2 = QtWidgets.QLabel(self.bot)
        self.label_2.setGeometry(QtCore.QRect(820, 10, 178, 18))
        self.label_2.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: #fff;\n"
"font-weight: bold;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.bot)
        TelaFinal.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaFinal)
        QtCore.QMetaObject.connectSlotsByName(TelaFinal)

    def retranslateUi(self, TelaFinal):
        _translate = QtCore.QCoreApplication.translate
        TelaFinal.setWindowTitle(_translate("TelaFinal", "MainWindow"))
        self.label_4.setText(_translate("TelaFinal", "Tudo pronto!"))
        self.textBrowser.setHtml(_translate("TelaFinal", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">Você receberá as informações personalizadas no número informado.</span></p></body></html>"))
        self.label_5.setText(_translate("TelaFinal", "Obrigada!"))
        self.label_2.setText(_translate("TelaFinal", "2022 CopyRight © Solutech"))
#import images_rc
