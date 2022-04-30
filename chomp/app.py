import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow
)

from Chomp import Chomp
from end_window_ui import Ui_endGame
from game_utils import *
from help_window_ui import Ui_helpWIndow
from main_window_ui import Ui_mainMenuWindow
from players import PLAYERS
import time


class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(tuple)
    time = QtCore.pyqtSignal(float)

    def __init__(self, game: Game, player1, player2, n=100, debug=False):
        super().__init__()
        self.game = game
        self.player1 = player1
        self.player2 = player2
        self.n = n
        self.debug = debug

    def run(self):
        start = time.time()
        p1_won = 0
        p2_won = 0
        draws = 0
        for _ in range(self.n):
            result = judge(self.game, self.player1, self.player2) if not self.debug else self.judge_debug(self.game, self.player1, self.player2)
            if result == 1:
                p1_won += 1
            elif result == 2:
                p2_won += 1
            else:
                draws += 1
            self.progress.emit((p1_won, p2_won))
        self.time.emit(time.time() - start)
        self.finished.emit()

    def stop(self):
        self.threadactive = False
        self.wait()

class Window(QMainWindow, Ui_mainMenuWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.thread = QtCore.QThread()

    def connectSignalsSlots(self):
        self.helpButton.clicked.connect(self.openHelpWindow)

    def openHelpWindow(self):
        helpWindow = HelpWindow()
        print("Opening help window...")
        helpWindow.exec_()
        print("Help window closed")

    def initialize(self):
        if self.startButton.text() == 'Graj':
            self.initializeGame()
        else:
            self.initializeTests()

    def initializeTests(self):
        self.stackedWidget.setCurrentIndex(3)

    def runTests(self):
        numTests = self.nTestsComboBox.value()
        self.thread = QtCore.QThread()
        self.worker = Worker(Chomp(self.width, self.height),
                             PLAYERS[self.player1_name], PLAYERS[self.player2_name], numTests, False)

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.time.connect(lambda x: self.timeLabel.setText(str(round(x, 4)) + 's'))
        self.worker.progress.connect(self.updateProgress)

        self.thread.start()

    def updateProgress(self, res):
        self.p1WinsLabel.setText(str(res[0]))
        self.p2WinsLabel.setText(str(res[1]))


    def initializeGame(self):
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
