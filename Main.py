from teeko import Board, Match, Player


def play():
    board = Board()
    board.initializateboard()
    player1 = Player("black")
    # player2 = Player("red")
    match = Match(board)
    # Llama a place marker hasta que sea 4 piezas por persona
    # se debe validar que un input no solape al otro
    # recibe input player1
    board.place_marker(1, 0, "black")
    # recibe input player2
    board.place_marker(1, 1, "red")
    # muestra estado del tablero
    mat = board.__str__()
    print(mat)
    pr = match.boardlimits(4, 4)
    print(pr)



play()
