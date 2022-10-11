# Libraries
import numpy as np


# Falta: verificar winner, corregir adyacente, out of range

# Generating board


class Board:

    def __init__(self, size=5):
        self.size = size
        self.cells = []

    def __str__(self):
        matrix = ""
        for row in self.cells:
            for cell in row:
                matrix = matrix + str(cell) + '  '
            matrix = matrix + "\n"
            c = + 1
        return matrix

    def initializateboard(self):
        for j in range(self.size):
            row = []
            for i in range(self.size):
                row.append(Cell(i, j, None))
            self.cells.append(row)

    def place_marker(self, posX, posY, marker):
        position = self.cells[posY][posX]
        position.contains = marker

    def remove_marker(self, posX, posY):
        position = self.cells[posY][posX]
        position.contains = None


# Generates a cell~~
class Cell:
    def __init__(self, posX, posY, contains):
        self.posX = posX
        self.posY = posY
        self.contains = contains

    def __str__(self):
        if self.contains == None:
            return "0"
        if self.contains == "black":
            return "1"
        if self.contains == "red":
            return "2"


class Match:
    def __init__(self, board):
        self.board = board

    def boardlimits(self, posX, posY):
        limitX = (posX >= 0) and (posX < self.board.size)
        limitY = (posY >= 0) and (posY < self.board.size)
        return limitX and limitY

    def on_range(self, posX, posY):
        limitX = (posX >= 0) and (posX <= self.board.size)
        limitY = (posY >= 0) and (posY <= self.board.size)
        return limitX and limitY

    # Valid once we placed the markers
    def adyacentMove(self, cell):
        actions = []
        directions = [
            [-1, -1], [-1, 0], [-1, +1],
            [0, -1], [0, +1],
            [+1, -1], [+1, 0], [+1, +1],
        ]

        for i in directions:
            adx = int(cell.posX) + i[0]
            ady = int(cell.posY) + i[1]
            if self.boardlimits(adx, ady):
                matrix = self.board.cells[ady][adx]
                if str(matrix.contains) == "None":
                    actions.append([ady, adx])

        return actions

    def isAdy(self, cell, actions):
        adx = int(cell.posX)
        ady = int(cell.posY)
        if [ady, adx] in actions:
            return True
        return False

    def isValid(self, cell, enemycolor):
        matrix = self.board.cells
        if self.boardlimits(cell.posX, cell.posY):

            if matrix[cell.posY][cell.posX].contains == enemycolor:
                print('ya existe una pieza enemiga aqui')
                return False
            if matrix[cell.posY][cell.posX].contains == cell.contains:
                print('ya existe una pieza tuya aqui')
                return False
            else:
                return True

    def isPlayers(self, cell, playercolor):
        matrix = self.board.cells
        if self.boardlimits(cell.posX, cell.posY):
            if matrix[cell.posY][cell.posX].contains == cell.contains:
                return True
        return False

    # Validation for a winner

    def horizontal(self, goal):
        matrix = self.board.cells

        for i in range(5):
            red = 0
            black = 0
            for j in range(5):
                cell = matrix[i][j]
                if cell.contains == "black":
                    black += 1
                else:
                    black = 0
                if cell.contains == "red":
                    red += 1
                else:
                    red = 0
                if black == 4:
                    return 1
                if red == 4:
                    return -1
        return None

    def vertical(self, goal):
        matrix = self.board.cells
        red = 0
        black = 0
        for j in range(5):

            for i in range(5):
                cell = matrix[i][j]
                if cell.contains == "black":
                    black += 1
                else:
                    black = 0
                if cell.contains == "red":
                    red += 1
                else:
                    red = 0
                if black == 4:
                    return 1
                if red == 4:
                    return -1
        return None

    def diagonal(self, goal):
        matrix = self.board.cells
        for i in range(5):
            for j in range(5):
                if self.boardlimits(i+2, j-2) or self.boardlimits(i+2, j+2) or self.boardlimits(i+1, j-1) or self.boardlimits(i+1, j+1) or self.boardlimits(i+3, j+3) or self.boardlimits(i+3, j-3):
                    if (j < 3 and i < 3):
                        if matrix[i][j].contains == "black" and matrix[i+1][j+1].contains == "black" and matrix[i+2][j+2].contains == "black" and matrix[i+3][j+3].contains == "black":
                            return 1
                        elif matrix[i][j].contains == "red" and matrix[i+1][j+1].contains == "red" and matrix[i+2][j+2].contains == "red" and matrix[i+3][j+3].contains == "red":
                            return -1
                    elif (j >= 3 and i < 3):
                        if matrix[i][j].contains == "black" and matrix[i+1][j-1].contains == "black" and matrix[i+2][j-2].contains == "black" and matrix[i+3][j-3].contains == "black":
                            return 1
                        elif matrix[i][j].contains == "red" and matrix[i+1][j-1].contains == "red" and matrix[i+2][j-2].contains == "red" and matrix[i+3][j-3].contains == "red":
                            return -1
        return None

    def square(self, goal):
        matrix = self.board.cells
        for i in range(5):
            for j in range(5):
                if self.boardlimits(i+2, j-2) or self.boardlimits(i+2, j+2) or self.boardlimits(i+1, j-1) or self.boardlimits(i+1, j+1) or self.boardlimits(i+3, j+3) or self.boardlimits(i+3, j-3):
                    if (j < 3):
                        if matrix[i][j].contains == "black" and matrix[i+1][j].contains == "black" and matrix[i][j+1].contains == "black" and matrix[i+1][j+1].contains == "black":
                            return 1
                    elif (j >= 3 and i < 3):
                        if matrix[i][j].contains == "red" and matrix[i+1][j].contains == "red" and matrix[i][j+1].contains == "red" and matrix[i+1][j+1].contains == "red":
                            return -1
        return None

    def checkWinner(self):
        winner = self.horizontal(self)
        if winner != None:
            return winner
        winner = self.vertical(self)
        if winner != None:
            return winner
        winner = self.diagonal(self)
        if winner != None:
            return winner
        winner = self.square(self)
        if winner != None:
            return winner

        return winner

    def shoWinner(self, winner):
        if winner == 1:
            print("Black markers win")
        elif winner == -1:
            print("Red markers win")


class Player:
    def __init__(self, playerColor):
        self.playerColor = playerColor
