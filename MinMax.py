from teeko import Board, Match, Player, Cell
import numpy as np


class State:
    def __init__(self, match):
        self.match = match
        self.utility = 0
        self.max_depth = 3

    def __str__(self):
        return self.match.board_status()

    def copy(self):
        copySate = State(self.match)
        return copySate

    def result(self, action):
        p1y = action[0]
        p1x = action[1]
        #state = state.copy()
        self.match.board.place_marker(p1y, p1x, 'red')
        return self

    def terminal_test(self):
        return self.match.checkWinner()

    def Actions(self):
        matrix = self.match.board.cells
        actions = []
        for i in range(5):
            for j in range(5):
                if matrix[i][j].contains == 'red' and self.match.countPieces() >= 8:
                    actions.append(self.match.adyacentMove(matrix[i][j]))
                elif matrix[i][j].contains == None and self.match.countPieces() < 8:
                    actions.append([i, j])

        # print(actions)
        # print(len(actions))
        return actions

    def utility_function(self):
        matrix = self.match.board.cells
        # piezas juntas max +1 | si de adyacente tiene max se suma puntos, si de adyacente tiene min se restan
        # piezas juntas min -1 | si de adyacente tiene min se resta puntos, si es max se suman
        # si el oponente tiene una pieza junto a otra es correcto obstaculizarlo

        winner = self.match.checkWinner()
        value = 0
        if winner != None:
            return 100 * self.match.checkWinner()
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

    def cut_of(self, depth):
        if (depth == self.max_depth or self.terminal_test() != None):
            return True
        else:
            return False


class IA:
    def __init__(self, initialState):
        self.initalState = initialState
        self.max_depth = 3

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

        # print(actions)
        # print(len(actions))
        return actions

    def Result(self, state, action, player):
        p1y = action[0]
        p1x = action[1]
        state.match.board.place_marker(p1y, p1x, player.playerColor)
        return state

    def result(self, state, action):
        p1y = action[0]
        p1x = action[1]
        #state = state.copy()
        state.match.board.place_marker(p1y, p1x, 'red')
        return state

    def minmax_decision(self, initialState, player):
        actions = self.Actions(initialState)
        if player.playerColor == "black":
            values = []
            for a in actions:
                v = self.min_value(self.result(initialState, a))
                values.append(v)
            idx = np.argmax(values)
            return self.Actions(initialState)[idx]
        else:
            values = []
            for a in self.Actions(initialState):
                v = self.max_value(self.result(initialState, a))
                values.append(v)
            idx = np.argmin(values)
            return self.Actions(initialState)[idx]

    def min_value(self, state):
        if self.terminal_test(state):
            return state.match.checkWinner()
        actions = self.Actions(state)
        v = 10000
        for a in actions:
            v = min(v, self.max_value(self.result(state, a)))
        return v

    def max_value(self, state):
        if self.terminal_test(state):
            return state.match.checkWinner()
        actions = self.Actions(state)
        # array visitados
        # si result da un estado visitado ignorar
        v = -10000
        for a in actions:
            v = max(v, self.min_value(self.result(state, a)))
        return v

    # Alpha Beta

    def minmax_decision_AB(self, initialState, player, alpha, beta):
        actions = self.Actions(initialState)
        if player.playerColor == "black":
            values = []
            for a in actions:
                v = self.min_value_AB(self.result(
                    initialState, a), alpha, beta)
                values.append(v)
            idx = np.argmax(values)
            return self.Actions(initialState)[idx]
        else:
            values = []
            for a in self.Actions(initialState):
                v = self.max_value_AB(self.result(
                    initialState, a), alpha, beta)
                values.append(v)
            idx = np.argmin(values)
            return self.Actions(initialState)[idx]

    def min_value_AB(self, state, alpha, beta):
        if self.terminal_test(state):
            return state.match.checkWinner()
        actions = self.Actions(state)
        v = 10000
        for a in actions:
            v = min(v, self.max_value_AB(self.result(state, a), alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def max_value_AB(self, state, alpha, beta):
        if self.terminal_test(state):
            return state.match.checkWinner()
        actions = self.Actions(state)
        v = -10000
        for a in actions:
            v = max(v, self.min_value_AB(self.result(state, a), alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    # MINMAX WITH DEPTH WITH ALPHA BETA

    '''def cut_of(state, depth):
        if (depth == state.max_depth or state.terminal_test(state) != None):
            return True
        else:
            return False'''

    def minmax_decision_WDAB(self, initialState, player, alpha, beta):
        actions = initialState.Actions()
        if player.playerColor == "black":
            values = []
            for a in actions:
                v = self.min_value_WDAB(initialState.result(
                    a), alpha, beta, 0)
                values.append(v)
            idx = np.argmax(values)
            return initialState.Actions()[idx]
        else:
            values = []
            for a in initialState.Actions():
                v = self.max_value_WDAB(initialState.result(
                    a), alpha, beta, 0)
                values.append(v)
            idx = np.argmin(values)
            return initialState.Actions()[idx]

    def min_value_WDAB(self, state, alpha, beta, depth):

        if state.cut_of(depth):
            return state.utility_function()
        actions = state.Actions()
        v = 10000
        for a in actions:
            v = min(v, self.max_value_WDAB(
                state.result(a), alpha, beta, depth+1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def max_value_WDAB(self, state, alpha, beta, depth):
        if state.cut_of(depth):
            return state.utility_function()
        actions = state.Actions()
        v = -10000
        for a in actions:
            v = max(v, self.min_value_WDAB(
                state.result(a), alpha, beta, depth+1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
    '''def cut_of(self, state, depth):
        if (depth == self.max_depth or self.terminal_test(state) != None):
            return True
        else:
            return False

    def minmax_decision_WDAB(self, initialState, player, alpha, beta):
        actions = self.Actions(initialState)
        if player.playerColor == "black":
            values = []
            for a in actions:
                v = self.min_value_WDAB(initialState.result(
                    a), alpha, beta, 0)
                values.append(v)
            idx = np.argmax(values)
            return self.Actions(initialState)[idx]
        else:
            values = []
            for a in self.Actions(initialState):
                v = self.max_value_WDAB(initialState.result(
                    a), alpha, beta, 0)
                values.append(v)
            idx = np.argmin(values)
            return self.Actions(initialState)[idx]

    def min_value_WDAB(self, state, alpha, beta, depth):
        if self.cut_of(state, depth):
            return self.utility_function(state)
        actions = self.Actions(state)
        v = 10000
        for a in actions:
            v = min(v, self.max_value_WDAB(
                state.result(a), alpha, beta, depth+1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def max_value_WDAB(self, state, alpha, beta, depth):
        if self.cut_of(state, depth):
            return self.utility_function(state)
        actions = self.Actions(state)
        v = -10000
        for a in actions:
            v = max(v, self.min_value_WDAB(
                state.result(a), alpha, beta, depth+1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v'''


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


def testMinmax_WDAB():
    alpha = -10000
    beta = 10000
    board = Board()
    board.initializateboard()
    playerOne = Player("black")
    playerTwo = Player("red")
    match = Match(board)
    initialState = State(match)
    stateCopy = initialState
    ia = IA(initialState)
    print(initialState)
    initialState.match.board.place_marker(0, 0, playerOne.playerColor)
    initialState.match.board.place_marker(0, 1, playerOne.playerColor)
    '''initialState.match.board.place_marker(0, 2, playerOne.playerColor)
    initialState.match.board.place_marker(0, 3, playerOne.playerColor)'''
    print(stateCopy)
    state = ia.minmax_decision_WDAB(stateCopy, playerTwo, alpha, beta)
    print(state)
    # match.board.place_marker(
    #   state[0][1], state[0][0], playerTwo.playerColor)
    print(initialState)


def testMinmax_AB():
    alpha = -10000
    beta = 10000
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
    state = ia.minmax_decision_AB(changedState, playerTwo, alpha, beta)
    print(state)


def testMinmax():
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
    state = ia.minmax_decision(changedState, playerTwo)
    print(state)


# testActions()
# play_game()
# testMinmax()
# testMinmax_AB()
testMinmax_WDAB()
# testUtilities()
