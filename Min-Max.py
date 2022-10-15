from teeko import Board, Match, Player, Cell


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
        matrix = state.match.board.cells
        # piezas juntas max +1 | si de adyacente tiene max se suma puntos, si de adyacente tiene min se restan
        # piezas juntas min -1 | si de adyacente tiene min se resta puntos, si es max se suman
        # si el oponente tiene una pieza junto a otra es correcto obstaculizarlo

        winner = state.match.checkWinner()
        value = 0
        if winner != None:
            return 100 * state.match.checkWinner()
        else:
            boardValues = [
                [0, 1, 0, 1, 0],
                [1, 2, 2, 2, 1],
                [0, 2, 3, 2, 0],
                [1, 2, 2, 2, 1],
                [0, 1, 0, 1, 0]
            ]
            for x in range(5):
                for y in range(5):
                    if matrix[x][y].contains == "black":
                        value = value + 1 * boardValues[x][y]
                    if matrix[x][y].contains == "red":
                        value = value + -1 * boardValues[x][y]
        return value

    def Actions(self, state):
        matrix = state.match.board.cells
        actions = []
        for i in range(5):
            for j in range(5):
                if matrix[i][j].contains == 'red' and state.match.countPieces() >= 8:
                    actions.append(state.match.adyacentMove(matrix[i][j]))
                elif matrix[i][j].contains == None and state.match.countPieces() < 8:
                    actions.append([i, j])

        print(actions)
        print(len(actions))
        return actions

    def Result(self, state, action, player):
        p1y = action[0]
        p1x = action[1]
        state.match.board.place_marker(p1y, p1x, player.playerColor)
        return state

    def minmax_decision(self, initialState, player):
        if player.playerColor == "black":
            # retorna una accion asociada al valor, plantear eso
            max = self.min_value(initialState)
            return max
        else:
            min = self.max_value(initialState)
            return min

    def min_value(self, state):
        actions = self.Actions(state)
        if self.terminal_test(state):
            return self.utility_function(state)
        v = 10000000
        for a in actions:
            v = min(v, self.max_value(self.Result(state, a,)))
        return v

    def max_value(self, state):
        actions = self.Actions(state)
        if self.terminal_test(state):
            return self.utility_function(state)
        v = -10000000
        for a in actions:
            v = max(v, self.min_value(state))
        return v


def testActions():
    board = Board()
    board.initializateboard()
    playerOne = Player("black")
    playerTwo = Player("red")
    match = Match(board)
    initialState = State(match)
    ia = IA(initialState)
    print(initialState)
    match.board.place_marker(0, 0, playerOne.playerColor)
    match.board.place_marker(0, 1, playerOne.playerColor)
    match.board.place_marker(0, 2, playerOne.playerColor)
    match.board.place_marker(0, 3, playerOne.playerColor)

    match.board.place_marker(1, 0, playerTwo.playerColor)
    match.board.place_marker(1, 1, playerTwo.playerColor)
    match.board.place_marker(1, 2, playerTwo.playerColor)
    match.board.place_marker(1, 3, playerTwo.playerColor)

    changedState = State(match)
    print(changedState)
    ia.Actions(changedState)
    ia.min_value(changedState)


def play_game():
    board = Board()
    board.initializateboard()
    playerOne = Player("black")
    playerTwo = Player("red")
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
    result = ia.Result(changedState, [4, 4], playerTwo)
    print(result)
    ia.min_value(changedState)

def testUtilities():
    board = Board()
    board.initializateboard()
    playerOne = Player("black")
    playerTwo = Player("red")
    match = Match(board)
    initialState = State(match)
    ia = IA(initialState)
    print(initialState)
    match.board.place_marker(1, 4, playerOne.playerColor)
    match.board.place_marker(0, 1, playerOne.playerColor)
    match.board.place_marker(0, 2, playerOne.playerColor)
    match.board.place_marker(0, 3, playerOne.playerColor)

    match.board.place_marker(1, 0, playerTwo.playerColor)
    match.board.place_marker(1, 1, playerTwo.playerColor)
    match.board.place_marker(1, 2, playerTwo.playerColor)
    match.board.place_marker(1, 3, playerTwo.playerColor)
    currentState = State(match)
    print(currentState)
    ut = ia.utility_function(currentState)
    print(ut)

# testActions()
# play_game()
testUtilities()