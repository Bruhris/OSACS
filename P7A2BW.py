# Boris Wang
# Assignment 2 - Battleship
# Computer Science 20, blk 3
# April 25, 2021

# This program is my own work - BW

import random


def gameEnd(win):
    if win == True:
        print("You hit all the ships!")
        choice = input("Do you want to play again (Y or N)? ")
        while choice.lower() != "n" and choice.lower() != "y":
            print("That is not a proper input!")
            choice = input("Do you want to play again (Y or N)? ")
        if choice.lower() == 'n':
            print("Thanks for playing and see you next time!")
            return False
        else:
            return True
    elif win == False:
        print("You ran out of moves!")
        choice = input("Do you want to play again (Y or N)? ")
        while choice.lower() != "n" and choice.lower() != "y":
            print("That is not a proper input!")
            choice = input("Do you want to play again (Y or N)? ")
        if choice.lower() == 'n':
            print("Thanks for playing and see you next time!")
            return False
        else:
            return True


def assignShipSpot(size):
    spots = {}
    for i in range(size-1):
        newSpot = random.randint(1, size)
        while newSpot in spots:
            newSpot = random.randint(1, size)
        spots[newSpot] = random.randint(1, size)
    return spots


def print_board(board):
    for row in board:
        print(" ".join(row))


if __name__ == "__main__":
    playing = True
    print("Welcome to Bruhris' game of Battleship!")
    print("There will be ships placed randomly on a grid and you must try and hit them based on their coordinate! (Starting from 1)")
    print("If you hit a ship, the spot will be replaced by a 'X' and if you miss a '*'")
    print("You will be given turns based on difficulty and if you run out without hitting all the ship, you will lose!")
    print("However if you hit all the ships within the turn given, you will win!")
    while playing == True:
        diff = input(
            "Do you want to play on Easy (E), Medium (M), Hard (H) or Perfection (P)? ")
        while diff.lower() != 'e' and diff.lower() != 'm' and diff.lower() != 'h' and diff.lower() != 'p':
            print("That is not a good output!")
            diff = input(
                "Do you want to play on Easy (E), Medium (M), Hard (H) or Perfection (P)? ")
        if diff.lower() == 'e':
            size = 3
            move = 4
            shipSpot = assignShipSpot(size)
        elif diff.lower() == 'm':
            size = 5
            move = 10
            shipSpot = assignShipSpot(size)
        elif diff.lower() == 'h':
            size = 7
            move = 20
            shipSpot = assignShipSpot(size)
        elif diff.lower() == 'p':
            size = 10
            move = 9
            shipSpot = assignShipSpot(size)

        board = []
        for x in range(size):
            board.append(["O"] * size)

        while bool(shipSpot) == True:
            print_board(board)
            if len(shipSpot) == 1:
                print("There is", len(shipSpot), "ships remaining")
            else:
                ("There are", len(shipSpot), "ships remaining")
            print("You have", str(move), "moves left")
            print("Select the spot you want to hit: ")

            row = input("Row: ")
            while row.isdigit() == False or int(row) > size or int(row) < 1:
                print("That is not a valid input")
                row = input("Row: ")
            column = input("Column: ")
            while column.isdigit() == False or int(column) > size or int(column) < 1:
                print("That is not a valid input")
                column = input("Column: ")

            row = int(row)
            column = int(column)
            if row in shipSpot:
                if column in shipSpot.values():
                    print("You've hit a ship!")
                    del shipSpot[row]
                    board[row-1][column-1] = "X"
                    move -= 1
                else:
                    print("You've missed!")
                    board[row-1][column-1] = "*"
                    move -= 1
            else:
                print("You've missed!")
                board[row-1][column-1] = "*"
                move -= 1

            if bool(shipSpot) == False:
                win = True
                break
            elif move == 0:
                win = False
                break

        playing = gameEnd(win)
