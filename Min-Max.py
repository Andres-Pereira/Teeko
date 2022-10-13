from teeko import Board, Match, Player, Cell

# implementar actions para que sea mas generico


class State:
    def __init__(self, match):
        self.match = match
        self.utility = 0

    def __str__(self):
        return self.match.board_status()


class IA:
    def __init__(self, initialState):
        self.initalState = initialState

    def terminal_test(self, state):
        return state.match.checkWinner()

    def utility_function(self, state):
        return 0

    def minmax_decision(self, initialState, player):
        if player.playerColor == "black":
            # retorna una accion asociada al valor, plantear eso
            max = self.min_value(initialState)
            return max
        else:
            min = self.max_value(initialState)
            return min

    def min_value(self, state):
        actions = []
        # Caso base, indica que estamos en una hoja del arbol
        if self.terminal_test(state):
            return self.utility_function(state)
        v = 10000000
        # iterar en actions
        v = min(v, self.max_value(state))
        return v

    def max_value(self, state):
        actions = []
        # Caso base, indica que estamos en una hoja del arbol
        if self.terminal_test(state):
            return self.utility_function(state)
        v = 10000000
        # iterar en actions
        v = max(v, self.min_value(state))
        return v

def play_game():
    board = Board()
    board.initializateboard()
    playerOne = Player("black")
    playerTwo = Player("white")
    match = Match(board)
    initialState = State(match)
    ia = IA(initialState)
    print(initialState)
    match.board.place_marker(0, 0, playerOne.playerColor)
    match.board.place_marker(0, 1, playerOne.playerColor)
    match.board.place_marker(0, 2, playerOne.playerColor)
    match.board.place_marker(0, 3, playerOne.playerColor)
    changedState = State(match)
    print(changedState)
    ia.min_value(changedState)

play_game()