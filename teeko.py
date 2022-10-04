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

    # check, only valid when we put the first 4 markers
    def freecells(self, enemyColor):
        freeCells = []
        matrix = self.board.cells
        # board limits?
        for list in matrix:
            for cell in list:
                if cell.contains != enemyColor:
                    freeCells.append(cell)
        return freeCells

    # in progress
    def validmove(self, freeCells, input):
        valid = False
        if input in freeCells:
            valid = True
        if (valid == False):
            print("Not a valid movement!")

        return valid

    def horizontal(self, goal=4):
        red = 0
        black = 0
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
        red = 0
        black = 0
        matrix = self.board.cells
        matrix[0][1]
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

    def move(self, Match, Input):
        valid = Match.validmove(self, Input)

        if valid == False:
            print("Invalid movement!")
            return valid