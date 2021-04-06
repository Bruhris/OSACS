# Boris Wang
# Assignment 2 - Hi-Lo Game
# Computer Science 20, blk 3
# February 17, 2021

# This program is my own work - BW

import random

def randomnumgenerator():
    randnum = random.randint(1,13)
    return randnum


def gameplay(risk,predict,points):
    if int(predict) == 0:
        randnum = randomnumgenerator()
        print("The number is",str(randnum))
        if randnum <= 6:
            print("YOU WIN!")
            print("You have",points+int(risk)*2,"points")
            points = points+int(risk)*2
            return points
        else:
            print("YOU LOSE")
            print("You have",points-int(risk),"points")
            points = points-int(risk)
        return points

    elif int(predict) == 1:
        randnum = randomnumgenerator()
        print("The number is,",str(randnum))
        if randnum >= 8:
            print("YOU WIN!")
            print("You have",points+int(risk)*2,"points")
            points = points+int(risk)*2
            return points
        else:
            print("YOU LOSE!")
            print("You have",points-int(risk),"points")
            points = points-int(risk)
        return points

#Extension
def goodbye(points):
    if points <=0:
        print("YOU RAN OUT OF POINTS! NOW YOU GET THIS MESSAGE: ")   
        print("( ͒ ु- •̫̮ – ू ͒)")
    elif points>=10000:
        print("WOW YOU HAVE",str(points),"POINTS!")
        print("░░░░░▒░░▄██▄░▒░░░░░░") 
        print("░░░▄██████████▄▒▒░░░")
        print("░▒▄████████████▓▓▒░░")
        print("▓███▓▓█████▀▀████▒░░")
        print("▄███████▀▀▒░░░░▀█▒░░")
        print("████████▄░░░░░░░▀▄░░")
        print("▀██████▀░░▄▀▀▄░░▄█▒░")
        print("░█████▀░░░░▄▄░░▒▄▀░░") 
        print("░█▒▒██░░░░▀▄█░░▒▄█░░") 
        print("░█░▓▒█▄░░░░░░░░░▒▓░░")
        print("░▀▄░░▀▀░▒░░░░░▄▄░▒░░") 
        print("░░█▒▒▒▒▒▒▒▒▒░░░░▒░░░") 
        print("░░░▓▒▒▒▒▒░▒▒▄██▀░░░░") 
        print("░░░░▓▒▒▒░▒▒░▓▀▀▒░░░░") 
        print("░░░░░▓▓▒▒░▒░░▓▓░░░░░")
        print("░░░░░░░▒▒▒▒▒▒▒░░░░░░")


def main():
    game = True
    points = 1000

    print("The High Low Game\n")
    print("RULES:")
    print("1. Numbers 1 through 6 are low")
    print("2. Numbers 8 through 13 are high")
    print("3. Numbers 7 is neither high or low\n")  

    while game == True:
        print("You have",str(points),"points\n")
        amount = input("Enter points to risk: ")
        print("")
        highlow = input("Predict <1=High, 0=Low>: ")
        points = gameplay(amount,highlow,points)
        if points <=0:
            goodbye(points)
            keepplaying = input("Do you want to play again? (Y or N) ")
            if keepplaying.lower() == "y":
                points = 1000
            else:
                print("You ended the game with a Grand Total of:",str(points),"points")
                print("See you next time!")
                game = False
        else:
            goodbye(points)
            keepplaying = input("Do you want to play again? (Y or N) ")
            if keepplaying.lower() == "y":
                decide = input("Do you want to keep your current points or restart? (R or K) ")
                if decide.lower() == "r":
                    points = 1000
            else:
                print("You ended the game with a Grand Total of:",str(points),"points")
                print("See you next time!")
                game = False

if __name__ == "__main__":
    main()