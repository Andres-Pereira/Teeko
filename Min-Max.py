from teeko import Board, Match, Player, Cell

# implementar actions para que sea mas generico


class State:
    def __init__(self, match):
        self.match = match
        self.utility = 0

    def __str__(self):
        return self.match.board_status()

    def utility_function(self, state):
        return 0

    def terminal_test(self, player):
        actions = self.match.actions(player)
        return len(actions) == 0


    def min_value(self, state, player):
        actions = []
        if state.terminal_test(player):
            return state.utility_function(state)
        v = 10000000



def play_game():
    board = Board()
    board.initializateboard()
    playerOne = Player("black")
    playerTwo = Player("white")
    match = Match(board)
    initialState = State(match)
    print(initialState)
    match.board.place_marker(0, 0, playerOne.playerColor)
    changedState = State(match)
    print(changedState)

play_game()