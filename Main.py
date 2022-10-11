from teeko import Board, Match, Player, Cell


def play():
    board = Board()
    board.initializateboard()
    player1 = Player("black")
    player2 = Player("red")
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
            cell = Cell(int(p1X)-1, int(p1Y), player1.playerColor)
            valid = match.isValid(
                cell, player2.playerColor)

        match.board.place_marker(int(p1X)-1, int(p1Y), player1.playerColor)

        mat = board.__str__()
        print(mat)

        print("Red's turn")
        valid = False
        while valid == False:
            pos = input("Enter a position: ")
            p2Y = pos[0]
            p2Y = charToNum[p2Y]
            p2X = pos[1]
            cell = Cell(int(p2X)-1, int(p2Y), player2.playerColor)
            valid = match.isValid(
                cell, player1.playerColor)

        match.board.place_marker(int(p2X)-1, int(p2Y), player2.playerColor)

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
            cell = Cell(int(p1X)-1, int(p1Y), player1.playerColor)
            playersMarker = match.isPlayers(cell, player1.playerColor)

        ad = match.adyacentMove(cell)
        match.board.remove_marker(int(p2X)-1, int(p2Y))

        valid = False
        ady = False
        while valid == False and ady == False:
            print("Where do you want to move?")
            print(ad)
            pos = input("Enter a position: ")
            p1Y = pos[0]
            p1Y = charToNum[p1Y]
            p1X = pos[1]
            cell = Cell(int(p1X)-1, int(p1Y), player1.playerColor)
            valid = match.isValid(
                cell, player2.playerColor, player1.playerColor)
            ady = match.isAdy(cell, ad)

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
            playersMarker = match.isPlayers(cell, player2.playerColor)

        ad = match.adyacentMove(cell)
        match.board.remove_marker(int(p2X)-1, int(p2Y))

        valid = False
        ady = False
        while valid == False and ady == False:
            print("Where do you want to move?")
            print(ad)
            pos = input("Enter a position: ")
            p2Y = pos[0]
            p2Y = charToNum[p2Y]
            p2X = pos[1]
            cell = Cell(int(p2X)-1, int(p2Y), player2.playerColor)
            valid = match.isValid(
                cell, player1.playerColor, player2.playerColor)
            ady = match.isAdy(cell, ad)

        match.board.place_marker(int(p1X)-1, int(p1Y), player1.playerColor)
        mat = board.__str__()
        print(mat)
        winner = match.checkWinner()

    match.shoWinner(winner)


play()
