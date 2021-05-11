import random
import copy


def assignPrizes(prizes, prizeBoard):
    for i in prizes:
        for k in range(3):
            boardX = random.randint(0, 4)
            boardY = random.randint(0, 4)
            while prizeBoard[boardX][boardY] != "[        ]":
                boardX = random.randint(0, 4)
                boardY = random.randint(0, 4)
            prizeBoard[boardX][boardY] = i


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
        return True
    # If yes, will continue the program
    else:
        return False


def print_board(board):
    for row in board:
        print("".join(row))


def check_Prize(prize):
    global puzzle, poster, ball, doll, game, endMessage
    if prize == "[ Puzzle ]":
        puzzle += 1
        if puzzle == 3:
            endMessage += "\nYou got a Puzzle!"
        return "Puzzle"
    elif prize == "[ Poster ]":
        poster += 1
        if poster == 3:
            endMessage += "\nYou got a Poster!"
        return "Poster"
    elif prize == "[  Ball  ]":
        ball += 1
        if ball == 3:
            endMessage += "\nYou got a Ball!"
        return "Ball"
    elif prize == "[  Doll  ]":
        doll += 1
        if doll == 3:
            endMessage += "\nYou got a Doll!"
        return "Doll"
    elif prize == "[  Game  ]":
        game += 1
        if game == 3:
            endMessage += "\nYou got a Game!"
        return "Game"


if __name__ == "__main__":
    board = []
    prizes = ["[ Puzzle ]", "[ Poster ]",
              "[  Ball  ]", "[  Doll  ]", "[  Game  ]"]
    puzzle = 0
    poster = 0
    ball = 0
    doll = 0
    game = 0
    pennies = 10
    endMessage = ""

    for x in range(5):
        board.append(["[        ]"] * 5)

    prizeBoard = copy.deepcopy(board)

    assignPrizes(prizes, prizeBoard)

    print_board(board)

    while pennies > 0:
        print()
        posX = random.randint(0, 4)
        posY = random.randint(0, 4)

        while prizeBoard[posX][posY] == "taken":
            posX = random.randint(0, 4)
            posY = random.randint(0, 4)

        if prizeBoard[posX][posY] != "[        ]":
            win = check_Prize(prizeBoard[posX][posY])
            print("You hit a", win+"!\n")
            board[posX][posY] = prizeBoard[posX][posY]
            prizeBoard[posX][posY] = "taken"
        else:
            print("You hit nothing!\n")
            board[posX][posY] = "[  NONE  ]"
            prizeBoard[posX][posY] = "taken"

        pennies -= 1
        print_board(board)

    if endMessage == "":
        endMessage += "\nYou didn't get any prizes : (\nBetter luck next time!"

    print(endMessage)
