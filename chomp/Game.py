class Game:
    @property
    def initial_state(self):
        ...
        return state

    def player(self, state):
        ...
        return playerno

    def actions(self, state):
        ...
        return actions

    def result(self, state, action):
        ...
        return new_state

    def is_terminal(self, state):
        ...
        return boolean

    def utility(self, state, player):
        ...
        return number

    def print_state(self, state):
        ...        
