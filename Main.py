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
        p1X = input("Enter the position X: ")
        p1Y = input("Enter the position Y: ")
        # check if free cell and board limits, repetir input en caso de invalido
        free = match.freecells(player2.playerColor)
        match.board.place_marker(int(p1X), int(p1Y), player1.playerColor)
        print("Red's turn")
        p2X = input("Enter the position X: ")
        p2Y = input("Enter the position Y: ")
        # check if free cell and board limits, repetir input en caso de invalido
        match.board.place_marker(int(p2X), int(p2Y), player2.playerColor)
        mat = board.__str__()
        print(mat)
    winner = match.checkWinner()

    while winner == None:
        print("Black's turn")
        p1X = input("Enter the position X: ")
        p1Y = input("Enter the position Y: ")
        cell = Cell(p1X, p1Y, player1.playerColor)
        ad = match.adyacentMove(cell)
        # Falta verificar if free cell and board limits, corregir lo de cell, repetir input en caso de invalido
        if cell in ad:
            match.board.place_marker(int(p1X), int(p1Y), player1.playerColor)
        winner = match.checkWinner()
        print("Red's turn")
        p2X = input("Enter the position X: ")
        p2Y = input("Enter the position Y: ")
        ad = match.adyacentMove(cell)
        # Falta verificar if free cell and board limits, repetir input en caso de invalido
        if cell in ad:
            match.board.place_marker(int(p2X), int(p2Y), player2.playerColor)
        winner = match.checkWinner()
    match.shoWinner(winner)


play()
