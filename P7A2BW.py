from random import random


def print_board(board):
    for row in board:
        print(" ".join(row))


if __name__ == "__main__":
    print("Welcome to Bruhris' game of Battleship!")
    board = []
    for x in range(10):
        board.append(["O"] * 10)
    print_board(board)

    print("Select the spot you want to hit: ")
    row = input("Row: ")
    while row.isdigit() == False or int(row) > 10 or int(row) < 0:
        print("That is not a valid input")
        row = input("Row: ")
    column = input("Column: ")
    while column.isdigit() == False or int(column) > 10 or int(column) < 0:
        print("That is not a valid input")
        column = input("Row: ")
