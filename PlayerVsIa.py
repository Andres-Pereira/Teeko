from teeko import Board, Match, Player, Cell
from MinMax import IA, State


def vs():
    alpha = -10000
    beta = 10000
    board = Board()
    board.initializateboard()
    player1 = Player("black")
    player2 = Player("red")
    match = Match(board)
    initialState = State(match)
    ia = IA(initialState)
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
    match = Match(board)
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

        match.board.place_marker(int(p1X)-1, int(p1Y), player1.playerColor)
        match.board.place_marker(0, 0, player1.playerColor)

        mat = board.__str__()
        print(mat)

        print("Red's turn")
        changedState = State(match)
        state = ia.minmax_decision_WDAB(initialState, player2, alpha, beta)
        print(state)
        match.board.place_marker(state[0][1], state[0][0], player2.playerColor)

        mat = board.__str__()
        print(mat)

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
        mat = board.__str__()
        print(mat)
        winner = match.checkWinner()

        print("Red's turn")
        playersMarker = False
        while playersMarker == False:
            print("Which marker do you want to move?")
            pos = input("Enter a position: ")
            p2Y = pos[0]
            p2Y = charToNum[p2Y]
            p2X = pos[1]
            if match.on_range(int(p2X), int(p2Y)):
                cell = Cell(int(p2X) - 1, int(p2Y), player2.playerColor)
                playersMarker = match.isPlayers(cell, player2.playerColor)
            else:
                print("Out of limits")

        ad = match.adyacentMove(cell)
        match.board.remove_marker(int(p2X)-1, int(p2Y))

        valid = False
        ady = False
        while valid == False:
            while ady == False:
                print("Where do you want to move?")
                print(ad)
                pos = input("Enter a position: ")
                p2Y = pos[0]
                p2Y = charToNum[p2Y]
                p2X = pos[1]
                if match.on_range(int(p2X), int(p2Y)):
                    cell = Cell(int(p2X)-1, int(p2Y), player2.playerColor)
                    valid = match.isValid(cell, player1.playerColor)
                    ady = match.isAdy(cell, ad)
                else:
                    print("Out of limits")

        match.board.place_marker(int(p2X)-1, int(p2Y), player2.playerColor)
        mat = board.__str__()
        print(mat)
        winner = match.checkWinner()

    match.shoWinner(winner)


vs()
