# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Help.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_helpWIndow(object):
    def setupUi(self, helpWIndow):
        helpWIndow.setObjectName("helpWIndow")
        helpWIndow.resize(537, 401)
        helpWIndow.setWindowIcon(QtGui.QIcon(":/Chomp/Chomp_icon.ico"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(helpWIndow.sizePolicy().hasHeightForWidth())
        helpWIndow.setSizePolicy(sizePolicy)
        helpWIndow.setMinimumSize(QtCore.QSize(537, 401))
        helpWIndow.setMaximumSize(QtCore.QSize(537, 401))
        helpWIndow.setAccessibleName("")
        helpWIndow.setAccessibleDescription("")
        helpWIndow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.5625, x2:1, y2:0.545, stop:0 rgba(0, 152, 137, 255), stop:1 rgba(71, 175, 88, 255));")
        helpWIndow.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(helpWIndow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.helpText_2 = QtWidgets.QLabel(helpWIndow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpText_2.sizePolicy().hasHeightForWidth())
        self.helpText_2.setSizePolicy(sizePolicy)
        self.helpText_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 87 20pt \"Arial Black\";\n"
"color: rgb(122, 75, 52)")
        self.helpText_2.setObjectName("helpText_2")
        self.verticalLayout.addWidget(self.helpText_2)
        self.helpText_1 = QtWidgets.QLabel(helpWIndow)
        self.helpText_1.setAutoFillBackground(False)
        self.helpText_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255)")
        self.helpText_1.setScaledContents(False)
        self.helpText_1.setWordWrap(True)
        self.helpText_1.setObjectName("helpText_1")
        self.verticalLayout.addWidget(self.helpText_1)
        self.okButton = QtWidgets.QPushButton(helpWIndow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy)
        self.okButton.setStyleSheet("background-color: rgb(122, 75, 52);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.okButton.setObjectName("okButton")
        self.verticalLayout.addWidget(self.okButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(helpWIndow)
        self.okButton.clicked.connect(helpWIndow.reject)
        QtCore.QMetaObject.connectSlotsByName(helpWIndow)

    def retranslateUi(self, helpWIndow):
        _translate = QtCore.QCoreApplication.translate
        helpWIndow.setWindowTitle(_translate("helpWIndow", "Pomoc"))
        self.helpText_2.setText(_translate("helpWIndow", "<html><head/><body><p align=\"center\">Pomoc</p></body></html>"))
        self.helpText_1.setText(_translate("helpWIndow", "<html><head/><body><p align=\"justify\">Gracz 1 i gracz 2 wykonują ruchy na przemian, dzieląc się czekoladą wymiarów n×m. W każdym ruchu gracz wybiera kostkę i zabiera ją razem ze wszystkimi kostkami na prawo i w dół od niej (cały prostokąt). Grają póki cała czekolada nie będzie zjedzona. Jednak każdy z nich chce uniknąć zjedzenia ostatniej kostki z lewego górnego narożnika, w której czają się brokuły. Ten kto weźmie kostkę z brokułami przegrywa.</p><p>Aby wybrać kostkę do zabrania podczas swojego ruchu, kliknij na nią myszką.</p<p>W przypadku gdy obaj gracze są ustawieni na boty, uruchomonie zostaną testy<br/></p></body></html>"))
        self.okButton.setText(_translate("helpWIndow", "OK"))
