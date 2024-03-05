import copy
import math

X = "X"
O = "O"
EMPTY = None

class Board:
    def __init__(self):
        self.board = [[EMPTY]*7 for _ in range(6)]
        self.player = "X"


    def display(self):
        a = ""
        for row in self.board:
            a += "|"
            for cell in row:
                a += " " if cell == None else cell
                a += "|"
            a += "\n"
        print(a)

    def drop(self, column):
        for i in range(6)[::-1]:
            if self.board[i][column] == None:
                self.board[i][column] = self.player
                break
        self.player = "X" if self.player == "O" else "O"
        self.display()

    
    def winner(self):
        # Check rows
        for row in self.board:
            for i in range(4):
                if row[i] == row[i+1] == row[i+2] == row[i+3] != EMPTY:
                    return row[i]
        
        # Check columns
        for col in range(7):
            for i in range(3):
                if self.board[i][col] == self.board[i+1][col] == self.board[i+2][col] == self.board[i+3][col] != EMPTY:
                    return self.board[i][col]
        
        # Check diagonals (top-left to bottom-right)
        for row in range(3):
            for col in range(4):
                if self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3] != EMPTY:
                    return self.board[row][col]
        
        # Check diagonals (top-right to bottom-left)
        for row in range(3):
            for col in range(3, 7):
                if self.board[row][col] == self.board[row+1][col-1] == self.board[row+2][col-2] == self.board[row+3][col-3] != EMPTY:
                    return self.board[row][col]
        
        # Check for a tie
        for row in self.board:
            if (any(cell == None for cell in row)):
                return None
        
        return "Tie"