from teeko import Board, Match, Player, Cell
from MinMax import IA, State


def vs():
    board = Board()
    match = Match(board)
    board.initializateboard()
    player1 = Player("black")
    player2 = Player("red")
    initialState = State(match)
    ia = IA(initialState)
    redPieces = []
    charToNum = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4

    }
    winner = None

    for i in range(4):
        print("Black's turn")
        valid = False
        while valid == False:
            pos = input("Enter a position: ")
            p1Y = pos[0]
            p1Y = charToNum[p1Y]
            p1X = pos[1]
            if match.on_range(int(p1X), int(p1Y)):
                cell = Cell(int(p1X)-1, int(p1Y), player1.playerColor)
                valid = match.isValid(cell, player2.playerColor)
            else:
                print("Out of limits")

        '''match.board.place_marker(0, 0, player1.playerColor)
        match.board.place_marker(1, 0, player1.playerColor)
        match.board.place_marker(2, 0, player1.playerColor)
        match.board.place_marker(3, 0, player1.playerColor)'''
        match.board.place_marker(int(p1X)-1, int(p1Y), player1.playerColor)
        changedState = State(match)
        print(changedState)
        print("Red's turn")
        valid = False

        while valid == False:
            state = ia.minmax_decision_WD(changedState, player2)
            if match.on_range(state[1], state[0]):
                cell = Cell(state[1], state[0], player2.playerColor)
                valid = match.isValid(cell, player1.playerColor)
            else:
                print("Out of limits")
        redPieces.append(state)
        print(state)
        match.board.place_marker(state[1], state[0], player2.playerColor)

        changedState = State(match)
        print(changedState)
    print(redPieces)
    winner = match.checkWinner()
    # ------------------------------------------------------------------------
    while winner == None:
        print("Black's turn")
        playersMarker = False
        while playersMarker == False:
            print("Which marker do you want to move?")
            pos = input("Enter a position: ")
            p1Y = pos[0]
            p1Y = charToNum[p1Y]
            p1X = pos[1]
            if match.on_range(int(p1X), int(p1Y)):
                cell = Cell(int(p1X)-1, int(p1Y), player1.playerColor)
                playersMarker = match.isPlayers(cell, player1.playerColor)
            else:
                print("Out of limits")

        ad = match.adyacentMove(cell)
        match.board.remove_marker(int(p1X)-1, int(p1Y))

        valid = False
        ady = False
        while valid == False:
            while ady == False:
                print("Where do you want to move?")
                print(ad)
                pos = input("Enter a position: ")
                p1Y = pos[0]
                p1Y = charToNum[p1Y]
                p1X = pos[1]
                if match.on_range(int(p1X), int(p1Y)):
                    cell = Cell(int(p1X)-1, int(p1Y), player1.playerColor)
                    valid = match.isValid(cell, player2.playerColor)
                    ady = match.isAdy(cell, ad)
                else:
                    print("Out of limits")

        match.board.place_marker(int(p1X)-1, int(p1Y), player1.playerColor)
        changedState = State(match)
        print(changedState)
        winner = match.checkWinner()

        print("Red's turn")
        playersMarker = False
        i = 0
        while playersMarker == False and i < 5:

            stateToRemove = redPieces[i]
            if match.on_range(stateToRemove[1], stateToRemove[0]):
                cell = Cell(stateToRemove[1],
                            stateToRemove[0], player2.playerColor)
                playersMarker = match.isPlayers(cell, player2.playerColor)
            else:
                print("Out of limits")
            i += 1

        print(stateToRemove)
        redPieces.remove(stateToRemove)
        #del redPieces[i]
        ad = match.adyacentMove(cell)
        match.board.remove_marker(stateToRemove[1], stateToRemove[0])
        valid = False
        ady = False
        changedState = State(match)

        # Aqui tuvimos demasiados problemas al validar si era un adyacente, ya que al no cumplirse se quedaba en un bucle infinito retornando
        # el mismo estado asi que ahora la ficha de la ia se mueve pero sin importarle que no sea  adyacente a la pieza seleccionada
        while valid == False:
            state2 = ia.minmax_decision_WD(
                changedState, player2)

            if match.on_range(state2[1], state2[0]):
                cell = Cell(state2[1], state2[0], player2.playerColor)
                valid = match.isValid(cell, player1.playerColor)
            else:
                print("Out of limits")

        match.board.place_marker(state2[1], state2[0], player2.playerColor)
        redPieces.append(state2)
        changedState = State(match)
        print(changedState)
        print(redPieces)
        winner = match.checkWinner()

    match.shoWinner(winner)


vs()
