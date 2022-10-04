# Libraries
import numpy as np


# Falta: verificar winner
# Mejorar: Input de un solo llamado, cambiar input a letra

# Generating board
class Board:
    def __init__(self, size=5):
        self.size = size
        self.cells = []

    def __str__(self):
        matrix = ""
        for row in self.cells:
            for cell in row:
                matrix = matrix + str(cell)
            matrix = matrix + "\n"
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


# Generates a cell
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

    # Only valid when we put the first 4 markers
    def freecells(self, enemyColor):
        freeCells = []
        matrix = self.board.cells
        # board limits?
        for list in matrix:
            for cell in list:
                if cell.contains != enemyColor:
                    freeCells.append(cell)
        return freeCells

    # Valid once we placed the markers
    def adyacentMove(self, cell):
        actions = []
        directions = [
            [-1, -1], [-1, 0], [-1, +1],
            [0, -1], [0, +1],
            [+1, -1], [+1, 0], [+1, +1],
        ]

        for i in directions:
            adx = cell.posX + i[0]
            ady = cell.posY + i[1]
            if self.boardlimits(adx, ady):
                actions.append([adx, ady])
            return actions

    # Validation for a winner
    def horizontal(self, goal=4):
        matrix = self.board.cells
        for list in matrix:
            red = 0
            black = 0
            for cell in list:
                if cell.contains == "black":
                    black += 1
                elif cell.contains == "red":
                    red += 1
                if black == goal:
                    return 1
                if red == goal:
                    return -1
        return None

    def vertical(self, goal=4):
        matrix = self.board.cells
        for j in range(5):
            red = 0
            black = 0
            for i in range(5):
                cell = matrix[j, i]
                if cell.contains == "black":
                    black += 1
                elif cell.contains == "red":
                    red += 1
                if black == goal:
                    return 1
                if red == goal:
                    return -1
        return None

    def diagonal(self, goal=4):
        return None

    def square(self, goal=4):
        return None

    def checkWinner(self, goal=4):
        winner = self.horizontal(self, goal)
        if winner != None:
            return winner
        winner = self.vertical(self, goal)
        if winner != None:
            return winner
        winner = self.diagonal(self, goal)
        if winner != None:
            return winner
        winner = self.square(self, goal)
        if winner != None:
            return winner

        return winner

    def shoWinner(winner):
        if winner == 1:
            print("Black markers win")
        elif winner == -1:
            print("Red markers win")


class Player:
    def __init__(self, playerColor):
        self.playerColor = playerColor
