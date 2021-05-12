import random
import copy


def assignPrizes(prizes, prizeBoard):
    for i in prizes:
        for k in range(3):
            # Places 3 of each prize on the board and has error check to see if prizes overlap
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
    # Checks to see if you hit a certain prize more than once and if you hit three, adds a message saying that you won a prize
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
    # Assigns board and prizes
    game = True
    board = []
    prizes = ["[ Puzzle ]", "[ Poster ]",
              "[  Ball  ]", "[  Doll  ]", "[  Game  ]"]
    while game == True:
        # Assign amount of prizes hit, amount of pennies and message at the end
        puzzle = 0
        poster = 0
        ball = 0
        doll = 0
        game = 0
        pennies = 10
        endMessage = ""

        for x in range(5):
            board.append(["[        ]"] * 5)
        # Creates a secret prize board with all the prizes
        prizeBoard = copy.deepcopy(board)
        # Assigns prizes on prize board
        assignPrizes(prizes, prizeBoard)

        print_board(board)

        while pennies > 0:
            print()
            # Selects a random point
            posX = random.randint(0, 4)
            posY = random.randint(0, 4)

            # Checks if point on board has already been hit by a penny
            while prizeBoard[posX][posY] == "taken":
                posX = random.randint(0, 4)
                posY = random.randint(0, 4)
            # If you hit something, then displays message and writes it on the board
            if prizeBoard[posX][posY] != "[        ]":
                win = check_Prize(prizeBoard[posX][posY])
                print("You hit a", win+"!\n")
                board[posX][posY] = prizeBoard[posX][posY]
                # Makes sure that the spot will not be hit again
                prizeBoard[posX][posY] = "taken"
            # If you hit nothing, then displays message and writes it on the board
            else:
                print("You hit nothing!\n")
                board[posX][posY] = "[  NONE  ]"
                # Makes sure that the spot will not be hit again
                prizeBoard[posX][posY] = "taken"

            pennies -= 1
            print_board(board)

        # If you didn't hit three prizes, you get a lose message
        if endMessage == "":
            endMessage += "\nYou didn't get any prizes : ( Better luck next time!"

        # Lists the amount of items that you hit and if you won any prizes
        print("You hit", puzzle, "puzzles")
        print("You hit", poster, "posters")
        print("You hit", ball, "balls")
        print("You hit", doll, "dolls")
        print("You hit", game, "games")
        print(endMessage)

        # Asks the user if they want to play Penny Pitch again
        game = goAgain()
