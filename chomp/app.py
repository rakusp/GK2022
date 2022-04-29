import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow
)

from Chomp import Chomp
from main_window_ui import Ui_mainMenuWindow
from help_window_ui import Ui_helpWIndow
from end_window_ui import Ui_endGame
from players import PLAYERS


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
        self.game = Chomp(self.height, self.width)
        self.player1, self.player2 = PLAYERS[self.player1_name], PLAYERS[self.player2_name]
        self.state = self.game.initial_state
        self.highlight_player(self.state[0])
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
                self.buttonList[y][x] = self.buttonList[y][x]#TODO co to robi?
        # switch to game page
        self.stackedWidget.setCurrentIndex(2)
        if self.player1 != None:
            action = self.player1(self.game, self.state)
            self.move(action)

    # opponent can also use this
    def chocolateClicked(self, x, y):
        print(self.player1_name, self.player2_name)
        print('Clicked piece:', (x, y))
        action = (y,x)
        if self.move(action):
            self.after_game()
            return

        print(f"Player's: {self.game.player(self.state)} turn")
        currentPlayer = self.player1 if self.game.player(self.state) == 1 else self.player2
        if currentPlayer != None:
            action = currentPlayer(self.game, self.state)
            if self.move(action):
                self.after_game()


    def move(self, action):
        """return if state is terminal"""
        self.state = self.game.result(self.state, action)
        self.updateBoardFromState()
        self.highlight_player(self.state[0])
        self.repaint()
        return self.game.is_terminal(self.state)

    def after_game(self):
        player_won = self.state[0]
        print(f'Game over, player {player_won} won')
        endWindow = EndWindow(self, player_won=player_won)
        endWindow.exec_()


    def updateBoardFromState(self):
        chococlate = self.state[1]
        m,n = chococlate.shape
        for i in range(self.height):
            for j in range(self.width):
                if chococlate[i][j] == 0:
                    self.buttonList[i][j].setEnabled(False)
                    self.buttonList[i][j].setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")



class HelpWindow(QDialog, Ui_helpWIndow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class EndWindow(QDialog, Ui_endGame):
    def __init__(self, mainWindow, parent=None, player_won=None):
        super().__init__(parent)
        print(player_won)
        self.set_player_won(player_won)
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
