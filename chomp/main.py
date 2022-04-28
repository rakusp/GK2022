#Simple example of how to run a game.
import time

from Chomp import Chomp
from Game import Game
from game_utils import judge, run_test
from players import alphabeta, random_agent, minimax


def play(game: Game, player1, player2):
    start = time.time()
    result = judge(game, player1, player2)
    d_time = time.time()-start
    print(f"Time elapsed: {d_time}")

    return result

a = None
for res in run_test(Chomp(5,5), alphabeta, minimax, 100):
    print(res)
