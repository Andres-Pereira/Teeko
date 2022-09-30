# Libraries
import numpy as np


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

    # maybe a redundant method?
    def enemycells(self, playerColor):
        matrix = self.board.cells
        enemies = []
        for list in matrix:
            for cell in list:
                if cell.contains != playerColor:
                    enemies.append(cell)
        return enemies

    def freecells(self, enemyColor):
        freeCells = []
        matrix = self.board.cells
        # board limits?
        for list in matrix:
            for cell in list:
                if cell.contains != enemyColor:
                    freeCells.append(cell)
        return freeCells

    # verify if the input is valid, in progress
    def validmove(self, playerColor, input):
        return True

    # funcion que revise si alguien gano, pendiente
    # funcion que revise estado del tablero, pendiente


class Player:
    def __init__(self, playerColor):
        self.playerColor = playerColor

    # action function, pendiente