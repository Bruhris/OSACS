# Boris Wang
# Assignment 4 - NIM
# Computer Science 20, blk 3
# March 3, 2021

# This program is my own work - BW

import random

def userInput(stones,user):
    print("There are",stones,"stones.", end = " ")
    #asks for how many stones you want to take
    takeaway = input("How many stones would you like to take? ")
    #runs it through the valid entry function to make sure that the user input makes sense
    decision = ValidEntry(takeaway, stones)
    if decision == "1":
        print(user,"has taken",decision,"stone!")
    else:
        print(user,"has taken",decision,"stones!")
    #returns the value of the stones taken
    return decision

def ValidEntry(decision, totalStones):
    #determines if user input is valid
    Valid = False
    while Valid != True:
        #checks if it is a integer
        if decision.isdigit() == False:
            print("That is not a valid amount of stones to take")
            decision = input("How many stones would you like to take? ")
        #checks if the input is between 1 and 3
        elif int(decision) < 1 or int(decision) >3:
            print("That is not a valid amount of stones to take")
            decision = input("How many stones would you like to take? ")
        #makes sure that user cannot take an illegal number of stones
        elif int(decision) > totalStones:
            print("That is not a valid amount of stones to take")
            decision = input("How many stones would you like to take? ")
        else:
            Valid = True
    #returns the value
    return decision

def restart():
    #asks the user if they want to play again
    option = input("Do you want to play again (Y or N) ")
    #if no, ends game
    if option.lower() == "n":
        print("See you next time!")
        return False
    #if yes, runs game again
    else:
        return True


def drawStones(stones):
    #makes sure that if the computer is placed in a losing situation, they try not to lose
    if stones == 2 or stones == 1:
        return 1
    elif stones == 3:
        return random.randint(1,2)
    else:
        #otherwise, picks a random number
        return random.randint(1,3)

def numStones():
    #creates a random number of stones for the game
    return random.randint(15,30)

def main():
    game = True
    gameStones = numStones()
    print("Welcome to Boris' NIM Game!")
    name = input("What is your name? ")
    print("Hi",name+"! Lets play the game NIM!")

    while game == True:
        #if computer takes the last game stone, user wins:
        if gameStones == 0:
            print(name,"has beaten the computer!")
            print(victory)
            game = restart()
            if game == True:
                gameStones = numStones()
            else:
                break
        #makes the user take away stones from the total stone pool
        userStones = userInput(gameStones,name)
        gameStones -= int(userStones)

        #if user takes the last game stone, computer wins
        if gameStones == 0:
            print("The computer has beaten",name+"!")
            print(defeat)
            game = restart()
            if game == True:
                gameStones = numStones()
            else:
                break

        #makes the computer take away stones from the total stone pool
        compStones = drawStones(gameStones)
        print("There are",gameStones,"stones.")
        if compStones == 1:
            print("The computer has taken",str(compStones)+" stone!")
        else:
            print("The computer has taken",str(compStones)+" stones!")
        gameStones -= compStones
        
if __name__ == "__main__":
    #when the player loses message
    defeat = """
                __████████_____██████
        _________█░░░░░░░░██_██░░░░░░█
        ________█░░░░░░░░░░░█░░░░░░░░░█
        _______█░░░░░░░███░░░█░░░░░░░░░█
        _______█░░░░███░░░███░█░░░████░█
        ______█░░░██░░░░░░░░███░██░░░░██
        _____█░░░░░░░░░░░░░░░░░█░░░░░░░░███
        ____█░░░░░░░░░░░░░██████░░░░░████░░█
        ____█░░░░░░░░░█████░░░████░░██░░██░░█
        ___██░░░░░░░███░░░░░░░░░░█░░░░░░░░███
        __█░░░░░░░░░░░░░░█████████░░█████████
        _█░░░░░░░░░░█████_████___████_█████___█
        _█░░░░░░░░░░█______█_███__█_____███_█___█
        █░░░░░░░░░░░░█___████_████____██_██████
        ░░░░░░░░░░░░░█████████░░░████████░░░█
        ░░░░░░░░░░░░░░░░█░░░░░█░░░░░░░░░░░░█
        ░░░░░░░░░░░░░░░░░░░░██░░░░█░░░░░░██
        ░░░░░░░░░░░░░░░░░░██░░░░░░░███████
        ░░░░░░░░░░░░░░░░██░░░░░░░░░░█░░░░░█
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
        ░░░░░░░░░░░█████████░░░░░░░░░░░░░░██
        ░░░░░░░░░░█▒▒▒▒▒▒▒▒███████████████▒▒█
        ░░░░░░░░░█▒▒███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
        ░░░░░░░░░█▒▒▒▒▒▒▒▒▒█████████████████
        ░░░░░░░░░░████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
        ░░░░░░░░░░░░░░░░░░██████████████████
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░██
        ▓██░░░░░░░░░░░░░░░░░░░░░░░░██
        ▓▓▓███░░░░░░░░░░░░░░░░░░░░█
        ▓▓▓▓▓▓███░░░░░░░░░░░░░░░██
        ▓▓▓▓▓▓▓▓▓███████████████▓▓█
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█\n"""

    #when the player wins message
    victory = """
                 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⠛⠃⠄⠄⠈⠉⠛⢿⣿⣿⣿
                 ⣿⣿⣿⣿⣿⣿⣿⣿⢿⣻⣯⠭⠤⠬⣉⣉⣛⣿⣿⣿⣶⣤⣀⠄⠈⠿⢿⣿
                 ⣿⣿⣿⣿⣿⠿⠙⢈⡩⠤⠶⠶⠶⠦⠤⠤⣉⡉⠛⢯⡙⠻⣿⣷⣆⠄⠄⢹
                 ⣿⣿⣿⠛⠁⠄⠊⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠒⢄⡈⢢⣈⠻⣿⡆⠄⢠
                 ⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢄⠻⣦⣘⣷⠄⢸
                 ⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠱⡈⢿⣿⠄⠘
                 ⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢁⠸⡟⠄⢠
                 ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠇⠄⣸
                 ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣿
                 ⡇⣿⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠼⠄⣿⣿
                 ⡇⣿⣿⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡠⠂⠄⣼⣿⣿
                 ⣿⡙⢿⣿⣷⣄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣤⠞⠁⢀⣼⣿⣿⣿
                 ⣿⣷⣤⣙⣿⣿⣿⣶⣤⣄⣀⣀⣀⣀⣀⣀⣤⣴⠾⠛⠁⢀⣠⣾⣿⣿⣿⣿
                 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠋⢉⣁⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿\n"""
    #runs all code under the main function, which runs the game
    main()