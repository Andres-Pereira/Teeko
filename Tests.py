from teeko import Board, Match, Player, Cell


def testSquare():
    board = Board()
    board.initializateboard()
    player1 = Player("black")
    player2 = Player("red")
    winner = None
    match = Match(board)

    match.board.place_marker(int(0), int(0), player1.playerColor)
    match.board.place_marker(int(1), int(0), player1.playerColor)
    match.board.place_marker(int(0), int(1), player1.playerColor)
    match.board.place_marker(int(1), int(2), player1.playerColor)

    match.board.place_marker(int(3), int(0), player2.playerColor)
    match.board.place_marker(int(4), int(0), player2.playerColor)
    match.board.place_marker(int(3), int(1), player2.playerColor)
    match.board.place_marker(int(4), int(1), player2.playerColor)

    print(board)
    winner = match.checkWinner()
    match.shoWinner(winner)


def testDiagonal():
    board = Board()
    board.initializateboard()
    player1 = Player("black")
    player2 = Player("red")
    winner = None
    match = Match(board)

    match.board.place_marker(int(0), int(0), player1.playerColor)
    match.board.place_marker(int(1), int(1), player1.playerColor)
    match.board.place_marker(int(2), int(2), player1.playerColor)
    match.board.place_marker(int(4), int(4), player1.playerColor)

    match.board.place_marker(int(1), int(0), player2.playerColor)
    match.board.place_marker(int(2), int(1), player2.playerColor)
    match.board.place_marker(int(3), int(2), player2.playerColor)
    match.board.place_marker(int(4), int(3), player2.playerColor)

    print(board)
    winner = match.checkWinner()
    match.shoWinner(winner)


def testDiagonal2():
    board = Board()
    board.initializateboard()
    player1 = Player("black")
    player2 = Player("red")
    winner = None
    match = Match(board)

    match.board.place_marker(int(0), int(4), player1.playerColor)
    match.board.place_marker(int(1), int(3), player1.playerColor)
    match.board.place_marker(int(2), int(2), player1.playerColor)
    match.board.place_marker(int(0), int(0), player1.playerColor)

    match.board.place_marker(int(1), int(4), player2.playerColor)
    match.board.place_marker(int(2), int(3), player2.playerColor)
    match.board.place_marker(int(3), int(2), player2.playerColor)
    match.board.place_marker(int(4), int(1), player2.playerColor)

    print(board)
    winner = match.checkWinner()
    match.shoWinner(winner)


def testHorizontal():
    board = Board()
    board.initializateboard()
    player1 = Player("black")
    player2 = Player("red")
    pX = 0
    winner = None
    match = Match(board)

    match.board.place_marker(int(1), int(2), player1.playerColor)
    match.board.place_marker(int(2), int(2), player1.playerColor)
    match.board.place_marker(int(3), int(2), player1.playerColor)
    match.board.place_marker(int(4), int(2), player1.playerColor)

    match.board.place_marker(int(0), int(1), player2.playerColor)
    match.board.place_marker(int(2), int(0), player2.playerColor)
    match.board.place_marker(int(3), int(0), player2.playerColor)
    match.board.place_marker(int(4), int(0), player2.playerColor)

    print(board)
    winner = match.checkWinner()
    match.shoWinner(winner)


def testVertical():
    board = Board()
    board.initializateboard()
    player1 = Player("black")
    player2 = Player("red")
    winner = None
    match = Match(board)

    match.board.place_marker(int(0), int(0), player1.playerColor)
    match.board.place_marker(int(0), int(2), player1.playerColor)
    match.board.place_marker(int(0), int(3), player1.playerColor)
    match.board.place_marker(int(0), int(4), player1.playerColor)

    match.board.place_marker(int(1), int(1), player2.playerColor)
    match.board.place_marker(int(1), int(2), player2.playerColor)
    match.board.place_marker(int(1), int(3), player2.playerColor)
    match.board.place_marker(int(1), int(4), player2.playerColor)

    print(board)
    winner = match.checkWinner()
    match.shoWinner(winner)


testSquare()
# testDiagonal2()
# testDiagonal()
# testVertical()
# testHorizontal()
