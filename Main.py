from teeko import Board, Match, Player, Cell


def play():
    board = Board()
    board.initializateboard()
    player1 = Player("black")
    player2 = Player("red")
    winner = None
    match = Match(board)
    for i in range(5):
        print("Black's turn")
        valid = False
        while valid == False:
            p1X = input("Enter the position X: ")
            p1Y = input("Enter the position Y: ")
            cell = Cell(int(p1X), int(p1Y), player1.playerColor)
            valid = match.isValid(cell, player2.playerColor)

        match.board.place_marker(int(p1X), int(p1Y), player1.playerColor)

        mat = board.__str__()
        print(mat)

        print("Red's turn")
        valid = False
        while valid == False:
            p2X = input("Enter the position X: ")
            p2Y = input("Enter the position Y: ")
            cell = Cell(int(p2X), int(p2Y), player2.playerColor)
            valid = match.isValid(cell, player1.playerColor)

        match.board.place_marker(int(p2X), int(p2Y), player2.playerColor)

        mat = board.__str__()
        print(mat)

    winner = match.checkWinner()
    # ------------------------------------------------------------------------
    while winner == None:
        print("Black's turn")
        playersMarker = False
        while playersMarker == False:
            print("Which marker do you want to move?")
            p1X = input("Enter the position X: ")
            p1Y = input("Enter the position Y: ")
            cell = Cell(int(p1X), int(p1Y), player1.playerColor)
            playersMarker = match.isPlayers(cell, player1.playerColor)

        ad = match.adyacentMove(cell)

        valid = False
        ady = False
        while valid == False and ady == False:
            print("Where do you want to move?")
            print(ad)
            p1X = input("Enter the position X: ")
            p1Y = input("Enter the position Y: ")
            cell = Cell(int(p1X), int(p1Y), player1.playerColor)
            valid = match.isValid(cell, player2.playerColor)
            ady = match.isAdy(cell, ad)

        if cell in ad:
            match.board.place_marker(int(p1X), int(p1Y), player1.playerColor)
        winner = match.checkWinner()

        print("Red's turn")
        valid = False
        while valid == False:
            p2X = input("Enter the position X: ")
            p2Y = input("Enter the position Y: ")
            cell = Cell(int(p2X), int(p2Y), player2.playerColor)
            valid = match.isValid(cell, player1.playerColor)

        ad = match.adyacentMove(cell)

        if cell in ad:
            match.board.place_marker(int(p2X), int(p2Y), player2.playerColor)
        winner = match.checkWinner()

    match.shoWinner(winner)


play()
