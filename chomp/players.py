import numpy as np

from Chomp import Chomp
from Game import Game
import random

from game_utils import opponent


def dummy(game, state):
    return game.actions(state)[0]


def random_agent(game, state):
    return random.choice(game.actions(state))


def middle_agent(game, start_state):
    def is_rectangle(board):
        n,m = board.shape
        i,j = 0,0
        while i+1 < n and board[i+1][j]:
            i+=1
        while j+ 1 < m and board[i][j+1]:
            j+=1
        if np.sum(board) == np.sum(board[0:(i+1),0:(j+1)]):
            return i,j
        return None

    def is_nxn(board):
        if not board[1,1]:
            return None
        ij = is_rectangle(board)
        if ij == None:
            return
        i,j = ij
        if i == j:
            return i,j
        return None

    def is_nx2(board):#if is rectangle
        ij = is_rectangle(board)
        if ij == None:
            return
        i,j = ij
        if i == 1 or j ==1:
            return i,j
        return None

    def is_nx1(board):
        ij = is_rectangle(board)
        if ij == None:
            return
        i,j = ij
        if i == 0 or j == 0:
            return i,j
        return None

    def is_corner(board):
        n,m = board.shape
        i,j = 0,0
        while i+1 < n and board[i+1][0]:
            i+=1
        while j+ 1 < m and board[0][j+1]:
            j+=1
        if np.sum(board) == (np.sum(board[0, 0:(j+1)]) + np.sum(board[0:(i+1), 0]) -1):
            return i,j
        return None

    def is_corner_uneven(board):
        ij = is_corner(board)
        if ij == None:
            return
        i,j = ij
        if i != j:
            return i,j
        return None

    def is_22_beneficial(board):
        if not board[1,1]:
            return None
        board_copy = board.copy()
        board_copy[1:,1:] = 0
        if not is_corner_uneven(board_copy):
            return 1,1
        return None

    def is_almost_nx2(board):
        n,m = board.shape
        if np.sum(board[2:, :]) == 0:
            j0 = 0
            while j0+1 < m and board[0, j0+1] == 1:
                j0 += 1
            j1 = 0
            while j1+1 < m and board[1, j1+1] == 1:
                j1 += 1
            if abs(j1-j0) == 1:
                return None
            return 0, j0, 1, j1
        elif np.sum(board[:, 2:]) == 0:
            i0 = 0
            while i0 + 1 < n and board[i0+1, 0] == 1:
                i0 += 1
            i1 = 0
            while i1 + 1 < n and board[i1+1, 1] == 1:
                i1 += 1
            if abs(i0-i1) == 1:
                return None
            return i0, 0, i1, 1
        return None

    def is_good(board):
        for check in [is_rectangle, is_corner_uneven, is_almost_nx2, is_22_beneficial, is_almost_nx2]:
            if check(board) is not None:
                return True
        return False

    _, start_board = start_state
    if np.sum(start_board) == 1:
        return 0,0
    ij = is_rectangle(start_board)
    if ij is not None:
        i,j = ij
        if i == 2 and j == 3:
            return (1,2)
        elif j == 2 and i == 3:
            return (2,1)
    ij = is_nxn(start_board)
    if ij is not None:
        return 1,1
    ij = is_22_beneficial(start_board)
    if ij is not None:
        i,j = ij
        return i,j
    ij = is_corner_uneven(start_board)
    if ij is not None:
        i,j = ij
        if i > j:
            return j+1,0
        return 0, i+1
    ij = is_nx1(start_board)
    if ij is not None:
        i,j = ij
        if i > j:
            return 1, 0
        return 0, 1
    ij = is_nx2(start_board)
    if ij is not None:
        i,j = ij
        if i > j:
            return i, 1
        return 1, j
    ijij = is_almost_nx2(start_board)
    if ijij is not None:
        i0,j0,i1,j1 = ijij
        if i0 == 0 and i1 == 1:
            if j0 >= j1:
                return i0,j1+2
            else:#to sie nigdy nie stanie :)
                return i1,j0
        else:
            if i0 >= i1:
                return i1+2,j0
            else:#to tez sie nigdy nie stanie :)
                return i0,j1
    actions = game.actions(start_state)
    if len(actions) == 1:
        return actions[0]
    actions = actions[1:]
    possible_actions = []
    bad_actions = []
    for action in actions:
        enemy_board = game.result(start_state, action)
        _, new_board = enemy_board
        if is_good(new_board):
            bad_actions.append((action, np.sum(new_board)))
        else:
            possible_actions.append(action)
    if len(possible_actions) > 0:
        return random.choice(possible_actions)
    else:
        #return random.sample(population=[b[0] for b in bad_actions], k=1,  counts=[b[1] for b in bad_actions])
        return random.choice([b[0] for b in bad_actions])


def minimax(game: Game, start_state):
    STATE_DICT = {}

    def max_move(state):
        key = str(state)
        if key in STATE_DICT:
            return STATE_DICT[key]
        if game.is_terminal(state):
            utility = game.utility(state, game.player(start_state))
            STATE_DICT[key] = utility
            return utility
        actions = game.actions(state)
        value = max([min_move(game.result(state, action)) for action in actions])
        STATE_DICT[key] = value
        return value

    def min_move(state):
        key = str(state)
        if key in STATE_DICT:
            return STATE_DICT[key]
        if game.is_terminal(state):
            utility = game.utility(state, game.player(start_state))
            STATE_DICT[key] = utility
            return utility
        actions = game.actions(state)
        value = min([max_move(game.result(state, action)) for action in actions])
        STATE_DICT[key] = value
        return value

    available_actions = game.actions(start_state)
    if len(available_actions) == 1:
        return available_actions[0]
    available_actions = available_actions[1:]
    winning_actions = []
    losing_actions = []
    for action in available_actions:
        result = min_move(game.result(start_state, action))
        if result == 1:
            winning_actions.append(action)
        else:
            losing_actions.append(action)
    if len(winning_actions) > 0:
        return random.choice(winning_actions)
    return random.choice(losing_actions)


def alphabeta(game: Chomp, start_state):
    STATE_DICT={}

    def max_move(state, alpha, beta):
        key = str((alpha, beta,state))
        if key in STATE_DICT:
            return STATE_DICT[key]
        if game.is_terminal(state):
            return game.utility(state, game.player(start_state))
        max_value = float("-inf")
        for action in game.actions(state):
            value = min_move(game.result(state, action), alpha,beta)
            if value > max_value:
                max_value = value
                alpha = max(alpha, max_value)
            if value >= beta:
                STATE_DICT[key] = value
                return value
        STATE_DICT[key] = max_value
        return max_value

    def min_move(state, alpha, beta):
        key = str((alpha, beta,state))
        if key in STATE_DICT:
            return STATE_DICT[key]
        if game.is_terminal(state):
            utility = game.utility(state, game.player(start_state))
            STATE_DICT[key] = utility
            return utility
        min_value = float("inf")
        for action in game.actions(state):
            value = max_move(game.result(state, action), alpha, beta)
            if value < min_value:
                min_value = value
                beta = min(beta,min_value)
            if value <= alpha:
                STATE_DICT[key] = value
                return value
        STATE_DICT[key] = min_value
        return min_value

    actions = game.actions(start_state)
    if len(actions) == 1:
        return actions[0]
    actions = actions[1:]#we will fight till the end
    winning_actions = []
    losing_actions = []
    for action in actions:
            value = min_move(game.result(start_state, action), float("-inf"), float("inf"))
            if value == 1:
                winning_actions.append(action)
            else:
                losing_actions.append(action)
    if len(winning_actions) > 0:
        return random.choice(winning_actions)
    return random.choice(losing_actions)


PLAYERS = {
    "Random": random_agent,
    "MinMax": minimax,
    "AlphaBeta": alphabeta,
    "Użytkownik": None,
    "Middle": middle_agent
}

