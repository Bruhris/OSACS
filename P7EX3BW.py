# Boris Wang
# Exercise 3 - Tic Tac Toe in Python
# Computer Science 20, blk 3
# May 19, 2021

# This program is my own work - BW

import random


def goAgain():
    # Asks if the user wants to use the program again
    print("Do you want to go again? (Y or N)")
    choice = input()
    # If user does not input the expected input, will continually ask them
    while choice.lower() != 'y' and choice.lower() != 'n':
        print("That is an invalid response!")
        choice = input()
    # If no, will end the program
    if choice.lower() == 'n':
        print("See you next time!")
        return False
    # If yes, will continue the program
    else:
        return True


def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('\n   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |\n')


def checkSpace(pos):
    # Checks if the space in the board is occupied and if it is, returns false and if not, returns True
    global board
    if board[pos] == ' ':
        board[pos] = 'X'
        return True
    else:
        print("This space is occupied!")
        return False


def userSpace():
    # Asks the user for where they want to place their X on the board
    pos = input("Select the position you want you place your 'X' (1-9) ")
    while True:
        try:
            # Checks to see if input is an integer or if space is already occupiedthe board
            while int(pos) > 9 or int(pos) < 1:
                print("That is invalid!")
                pos = input(
                    "Select the position you want you place your 'X' (1-9) ")
            break
        except ValueError:
            # If not integer, will ask them again
            print("That is invalid!")
            pos = input(
                "Select the position you want you place your 'X' (1-9) ")
    return int(pos)


def checkWinner(board):
    # Checks to see if user or computer has won by checking whether or certain board spots have been filled by O's or X's
    if ((board[1] == 'O' and board[2] == 'O' and board[3] == 'O') or
        (board[4] == 'O' and board[5] == 'O' and board[6] == 'O') or
        (board[7] == 'O' and board[8] == 'O' and board[9] == 'O') or
        (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or
        (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or
        (board[3] == 'O' and board[6] == 'O' and board[9] == 'O') or
        (board[1] == 'O' and board[5] == 'O' and board[9] == 'O') or
            (board[3] == 'O' and board[5] == 'O' and board[7] == 'O')):
        return "Computer"
    elif ((board[1] == 'X' and board[2] == 'X' and board[3] == 'X') or
          (board[4] == 'X' and board[5] == 'X' and board[6] == 'X') or
          (board[7] == 'X' and board[8] == 'X' and board[9] == 'X') or
          (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or
          (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or
          (board[3] == 'X' and board[6] == 'X' and board[9] == 'X') or
          (board[1] == 'X' and board[5] == 'X' and board[9] == 'X') or
          (board[3] == 'X' and board[5] == 'X' and board[7] == 'X')):
        return "Player"
    # If the board is filled and no one has won, then it is a draw
    elif ((board[1] != ' ') and
          (board[2] != ' ') and
          (board[3] != ' ') and
          (board[4] != ' ') and
          (board[5] != ' ') and
          (board[6] != ' ') and
          (board[7] != ' ') and
          (board[8] != ' ') and
          (board[9] != ' ')):
        return "None"


def computerSpace(board):
    # Makes computer select a random space on board
    compSpot = random.randint(1, 9)
    while board[compSpot] != ' ':
        compSpot = random.randint(1, 9)

    board[compSpot] = 'O'
    print("The computer hits", str(compSpot)+"!")


def playGame(board):
    while True:
        # Inputs for user input and checks if it is valid
        pos = userSpace()
        check = checkSpace(pos)
        while check == False:
            pos = userSpace()
            check = checkSpace(pos)
        # Draws the board
        drawBoard(board)
        # Checks if the user has won yet
        winner = checkWinner(board)
        if winner == "Player":
            print("The Player Won!")
            game = goAgain()
            if game == False:
                # Returns false if player does not want to play again
                return False
            else:
                # Returns true if play wants to play again and clears board
                board.clear()
                return True
        elif winner == "None":
            print("It ends in a draw!")
            game = goAgain()
            if game == False:
                return False
            else:
                board.clear()
                return True
        # Checks if computer won
        computerSpace(board)
        drawBoard(board)
        winner = checkWinner(board)
        if winner == "Computer":
            print("The Computer Won!")
            game = goAgain()
            if game == False:
                return False
            else:
                board.clear()
                return True
        elif winner == "None":
            print("It ends in a draw!")
            game = goAgain()
            if game == False:
                return False
            else:
                board.clear()
                return True


if __name__ == "__main__":
    something = True
    print("Welcome to Boris' game of Tic Tac Toe!")
    while something == True:
        # Creates board and draws in each time the user plays the game
        board = [' '] * 10
        drawBoard(board)
        something = playGame(board)
