from Game import Game
import random


def dummy(game, state):
    return game.actions(state)[0]


def random_agent(game, state):
    return random.choice(game.actions(state))


def minimax(game: Game, start_state):
    STATE_DICT = {}

    def max_move(state):
        key = str((start_state[0],state))
        if key in STATE_DICT:
            return STATE_DICT[key]
        if game.is_terminal(state):
            return game.utility(state, game.player(start_state))
        actions = game.actions(state)
        value = max([min_move(game.result(state, action)) for action in actions])
        STATE_DICT[key] = value
        return value

    def min_move(state):
        key = str((start_state[0],state))
        if key in STATE_DICT:
            return STATE_DICT[key]
        if game.is_terminal(state):
            return game.utility(state, game.player(start_state))
        actions = game.actions(state)
        value = min([max_move(game.result(state, action)) for action in actions])
        STATE_DICT[key] = value
        return value

    available_actions = game.actions(start_state)
    best_action =None
    best_score = float("-inf")
    for action in available_actions:
        result = min_move(game.result(start_state, action))
        if result > best_score:
            best_score = result
            best_action = action
    return best_action


def alphabeta(game, start_state):
    STATE_DICT={}

    def max_move(state, alpha, beta):
        key = str((start_state[0],state))
        if key in STATE_DICT:
            return STATE_DICT[key]
        if game.is_terminal(state):
            return game.utility(state, game.player(start_state)), None
        max_value = float("-inf")
        for action in game.actions(state):
            value, action2 = min_move(game.result(state, action), alpha,beta)
            if value > max_value:
                max_value, best_action = value, action
                alpha = max(alpha, max_value)
            if value >= beta:
                STATE_DICT[key] = (value, best_action)
                return value, best_action
        STATE_DICT[key] = (max_value, best_action)
        return max_value, best_action

    def min_move(state, alpha, beta):
        key = str((start_state[0],state))
        if key in STATE_DICT:
            return STATE_DICT[key]
        if game.is_terminal(state):
            return game.utility(state, game.player(start_state)),None
        min_value = float("inf")
        for action in game.actions(state):
            value, action2 = max_move(game.result(state, action), alpha, beta)
            if value < min_value:
                min_value, best_action = value, action
                beta = min(beta,min_value)
            if value <= alpha:
                STATE_DICT[key] = (value, best_action)
                return value, best_action
        STATE_DICT[key] = (min_value, best_action)
        return min_value, best_action

    return max_move(start_state, float("-inf"), float("inf"))[1]
