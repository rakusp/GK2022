from Game import Game
import numpy as np

from game_utils import opponent


class Chomp(Game):
    def __init__(self, m=4, n=4):
        self.m = m
        self.n = n

    @property
    def initial_state(self):
        # 1st val is player, 2nd is playing board
        return (1, np.ones((self.m, self.n)))

    # which player's turn is it
    def player(self, state):
        return state[0]

    def actions(self, state):
        where = np.where(state[1]==1)
        return [xy for xy in zip(where[0], where[1])]

    def result(self, state, action):
        board = state[1].copy()
        assert board[action[0], action[1]] == 1
        assert state[0] in {1, 2}
        board[action[0]:, action[1]:] =  0
        next_player = opponent(state[0])
        return (next_player, board)

    def _has_line(self, state, player):
        board = state[1]
        for i in [0, 3, 6]:
            if board[i] == board[i+1] == board[i+2] == player:
                return True
        for i in [0, 1, 2]:
            if board[i] == board[i+3] == board[i+6] == player:
                return True
        if board[0] == board[3+1] == board[2*3+2] == player:
            return True
        if board[2] == board[3+1] == board[2*3] == player:
            return True
        return False

    def is_terminal(self, state):
        return np.sum(state[1]) == 0

    def utility(self, state, player):
        assert player in {1, 2}
        if not self.is_terminal(state):
            return np.sum(state[1])/(self.m*self.n*2)
        if state[0] == player:
            return 1
        return -1

    def print_state(self, state):
        print(f"Player turn: {state[0]}")
        print(state[1])
