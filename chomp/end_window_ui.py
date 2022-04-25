# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'End.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_endGame(object):
    def setupUi(self, endGame):
        endGame.setObjectName("endGame")
        endGame.resize(400, 211)
        endGame.setMinimumSize(QtCore.QSize(400, 211))
        endGame.setMaximumSize(QtCore.QSize(400, 211))
        endGame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.5625, x2:1, y2:0.545, stop:0 rgba(0, 152, 137, 255), stop:1 rgba(71, 175, 88, 255));")
        endGame.setModal(True)
        self.horizontalLayoutWidget = QtWidgets.QWidget(endGame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 150, 381, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playAgainButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.playAgainButton.setStyleSheet("background-color: rgb(122, 75, 52);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.playAgainButton.setObjectName("playAgainButton")
        self.horizontalLayout.addWidget(self.playAgainButton)
        self.backToMenu = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.backToMenu.setStyleSheet("background-color: rgb(122, 75, 52);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.backToMenu.setObjectName("backToMenu")
        self.horizontalLayout.addWidget(self.backToMenu)
        self.winnerLabel = QtWidgets.QLabel(endGame)
        self.winnerLabel.setGeometry(QtCore.QRect(10, 10, 381, 121))
        self.winnerLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 87 20pt \"Arial Black\";\n"
"color: rgb(255, 255, 255)")
        self.winnerLabel.setObjectName("winnerLabel")

        self.retranslateUi(endGame)
        QtCore.QMetaObject.connectSlotsByName(endGame)

    def retranslateUi(self, endGame):
        _translate = QtCore.QCoreApplication.translate
        endGame.setWindowTitle(_translate("endGame", "Koniec gry"))
        self.playAgainButton.setText(_translate("endGame", "Zagraj ponownie"))
        self.backToMenu.setText(_translate("endGame", "Wróć do menu"))
        self.winnerLabel.setText(_translate("endGame", "<html><head/><body><p align=\"center\">WYGRAŁ GRACZ 1</p></body></html>"))
