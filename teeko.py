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

    def remove_marker(self, posX, posY):
        position = self.cells[posY][posX]
        position.contains = None

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
        matrix = self.board.cells
        directions = [
            [-1, -1], [-1, 0], [-1, +1],
            [0, -1], [0, +1],
            [+1, -1], [+1, 0], [+1, +1],
        ]

        for i in directions:
            adx = int(cell.posX) + i[0]
            ady = int(cell.posY) + i[1]
            print(matrix[cell.posX][cell.posY].contains)
            if self.boardlimits(adx, ady) and str(matrix[cell.posX][cell.posY].contains) == "None":
                actions.append([adx, ady])

        return actions

    def isAdy(self, cell, actions):
        adx = int(cell.posX)
        ady = int(cell.posY)
        if [adx, ady] in actions:
            return True
        return False
    def isValid(self, cell, enemycolor, playercolor):
        matrix = self.board.cells
        print(matrix[cell.posX][cell.posY].contains)
        if self.boardlimits(cell.posX, cell.posY):
            if str(matrix[cell.posX][cell.posY].contains) == str(enemycolor):
                return False
            if str(matrix[cell.posX][cell.posY].contains) == str(playercolor):
                return False
            return True

    def isPlayers(self, cell, playercolor):
        matrix = self.board.cells
        if str(matrix[cell.posX][cell.posY].contains) == str(playercolor):
            return True
        return False
    # Validation for a winner

    def horizontal(self, goal=4):
        return None

    def vertical(self, goal=4):
        return None

    def diagonal(self, goal=4):
        return None

    def square(self, goal=4):
        return None

    def checkWinner(self, goal=4):
        winner = self.horizontal(goal)
        if winner != None:
            return winner
        winner = self.vertical(goal)
        if winner != None:
            return winner
        winner = self.diagonal(goal)
        if winner != None:
            return winner
        winner = self.square(goal)
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
