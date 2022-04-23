from Game import Game


def opponent(player):
    assert player in {1, 2}
    if player == 1:
        return 2
    else:
        return 1


def judge(game: Game, player1, player2):
    state = game.initial_state

    while not game.is_terminal(state):
        if game.player(state) == 1:
            action = player1(game, state)
            print("action",action)
        else:
            action = player2(game, state)
        game.print_state(state)
        print("Action:", action)
        print()
        state = game.result(state, action)

    game.print_state(state)
    print("Reached terminal state?", game.is_terminal(state))
    u1 = game.utility(state, 1)
    u2 = game.utility(state, 2)
    print("Utility for the 1st player", u1)
    print("Utility for the 2nd player", u2)
    if u1 > u2:
        print("Winner: 1st player")
        return 1
    elif u1 < u2:
        print("Winner: 2nd player")
        return 2
    else:
        return 0
        print("Draw")

