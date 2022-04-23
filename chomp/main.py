#Simple example of how to run a game.
import time

from Chomp import Chomp
from Game import Game
from game_utils import judge
from players import alphabeta


def play(game: Game, player1, player2):
    start = time.time()
    result = judge(game, player1, player2)
    d_time = time.time()-start
    print(f"Time elapsed: {d_time}")

    return result


play(Chomp(4,4), alphabeta, alphabeta)


