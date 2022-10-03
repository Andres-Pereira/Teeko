from teeko import Board, Match, Player


def play():
    board = Board()
    board.initializateboard()
    mat = board.__str__()
    print(mat)
    player1 = Player("black")
    # player2 = Player("red")
    match = Match(board)


play()
