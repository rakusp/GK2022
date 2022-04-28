import numpy as np

from Chomp import Chomp
from Game import Game
import random

from game_utils import opponent


def dummy(game, state):
    return game.actions(state)[0]


def random_agent(game, state):
    return random.choice(game.actions(state))


def middle_agent(game, state):
    return random.choice(game.actions(state))#TODO make it clever


def minimax(game: Game, start_state):
    STATE_DICT = {}

    empty_state = np.zeros(start_state[1].shape)
    for i in range(empty_state.shape[0] +1):
        for j in range(empty_state.shape[1] + 1):
            if i!=0 and j!= 0:
                empty_state[0:i,0:j] = 1
                STATE_DICT[str((start_state[0], empty_state))] = 1
                STATE_DICT[str((opponent(start_state[0]), empty_state))] = -1

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
    if len(available_actions) == 0:
        return available_actions[0]
    available_actions = available_actions[1:]
    winning_actions = []
    losing_actions = []
    for action in available_actions:
        result = min_move(game.result(start_state, action))
        if result == 1:
            winning_actions.append(action)
        else:
            losing_actions.append(result)
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
    "random": random_agent,
    "MinMax": minimax,
    "AlphaBeta": alphabeta,
    "Użytkownik": None
}
