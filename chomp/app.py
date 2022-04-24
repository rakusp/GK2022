import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow
)



from main_window_ui import Ui_mainMenuWindow
from help_window_ui import Ui_helpWIndow
from end_window_ui import Ui_endGame


class Window(QMainWindow, Ui_mainMenuWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.helpButton.clicked.connect(self.openHelpWindow)

    def openHelpWindow(self):
        helpWindow = HelpWindow()
        print("Opening help window...")
        helpWindow.exec_()
        print("Help window closed")

    def initializeGame(self):

        # Tutaj mozna zrobic inicjalizacje AI
        # string nazwy wybranych graczy jest pod self.player1 i self.player2
        # może używać tej samej funkcji chocolateClicked co gracz, tylko na koncu check do kogo nalezy kolejny ruch

        self.chocolateLayout.setSpacing(24 - self.width - self.height)
        sizePolicy5 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        # create chocolate pieces
        for x in range(self.width):
            for y in range(self.height):
                self.buttonList[y][x] = QtWidgets.QPushButton(self.gridLayoutWidget)
                sizePolicy5.setHeightForWidth(self.buttonList[y][x].sizePolicy().hasHeightForWidth())
                self.buttonList[y][x].setSizePolicy(sizePolicy5)
                if x == 0 and y == 0:
                    # broccoli piece
                    self.buttonList[y][x].setStyleSheet(u"background-color: rgb(0, 170, 0);")
                else:
                    self.buttonList[y][x].setStyleSheet(u"background-color: rgb(122, 75, 52);")
                self.buttonList[y][x].clicked.connect(lambda ch, arg1=x, arg2=y: self.chocolateClicked(arg1, arg2))
                self.chocolateLayout.addWidget(self.buttonList[y][x], x, y, 1, 1)
                self.buttonList[y][x] = self.buttonList[y][x]
        # switch to game page
        self.stackedWidget.setCurrentIndex(2)

    # opponent can also use this
    def chocolateClicked(self, x, y):
        print('Clicked piece:', (x, y))
        for i in range(x, self.width):
            for j in range(y, self.height):
                # disable and hide (make transparent) all pieces to the right and below
                self.buttonList[j][i].setEnabled(False)
                self.buttonList[j][i].setStyleSheet(u"background-color: rgb(122, 75, 52, 0);")
        if x == 0 and y == 0:
            print('Game over')
            endWindow = EndWindow(self)
            endWindow.exec_()
        # TODO SWITCH PLAYER


class HelpWindow(QDialog, Ui_helpWIndow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class EndWindow(QDialog, Ui_endGame):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.setupEvents()

    def setupEvents(self):
        self.backToMenu.clicked.connect(self.returnToMenu)
        self.playAgainButton.clicked.connect(self.restartGame)

    def returnToMenu(self):
        self.mainWindow.stackedWidget.setCurrentIndex(0)
        self.reject()

    def restartGame(self):
        self.mainWindow.initializeGame()
        self.reject()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())