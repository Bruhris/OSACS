# Boris Wang
# Assignment 2 - Guessing Game
# Computer Science 20, blk 3
# February 17, 2021

# This program is my own work - BW

import random
randnum = random.randint(1,100)
tries = 0

print("Guessing game\n")
print("Instructions:  Try to guess the number between 1 and 100.\n")
num = input("Enter number (1 to 100): ")
tries += 1

while int(num) != randnum:
    while int(num)>randnum:
        num = input("Too high! Enter number (1 to 100): ")
        tries+=1

    while int(num)<randnum:
        num = input("Too low! Enter number (1 to 100): ")
        tries+=1

if int(num) == randnum:
    print("")
    print("That's correct!\n")
    print("It took you",tries,"tries to correctly guess",randnum)

#Extension
#if tries==1:
 #   print("WOW, you guessed it in one guess! As a reward you get this!")
#    print(" / \__")
  #  print("(    @\___")
  #  print("/         O") 
 #   print("/   (_____/")    
 #   print("/_____/   U") 
