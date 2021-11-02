# * ***********************************************************************
# Boris Wang
# Exercise 2 - Date Guessing Game
# Computer Science 30 - Block 6
# October 16, 2021

# This program is my own work - BW

# Day of the Year guessing game

import random

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"] # Assigns the months of the year
num_days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # Assigned the number of days corresponding to each month


def calendar(month_names, num_days_in_month):

    if len(month_names) != len(num_days_in_month): # If the # of dates do not match with the months, returns an empty list
        return []

    dates = [] # Creates an empty list and a counter variable idx
    idx = 0

    while idx < len(month_names): # Goes through every month in the list month_names
        for date in range(1, num_days_in_month[idx] + 1): # Gets every day in that month from 1 to the last day
            dates.append(month_names[idx] + " " + str(date)) # Adds the string with the month and date to the dates list
        idx = idx + 1 # Adds 1 to idx to go to next month until it reaches the end
    return dates # Returns the list of dates


first = calendar(month_names, num_days_in_month) # Creates first list that contains the entire years worth of dates


def guess_game(first = calendar(month_names, num_days_in_month), count = 1):
    if count == 1: # For the first date, starts at a random one within the list of dates
        mid = random.randint(0,len(first)-1)
        count-=1
    else:
        mid = len(first)//2 # Gets the middle index of the list filled with the dates

    val = is_earlier(first[mid]) # Checks if the guessed date is earlier, later or equal to the players guessed day

    if val == 1:
        return guess_game(first[:mid + 1], count) # If the date is earlier, will get all the dates that are before the index of the guessed date in list and run guess_game again with list split in half
    elif val == 2:
        return guess_game(first[mid - 1:], count) # If the date is later, will get all the dates that are before the index of the guessed date in list and runs guess_game again with list split in half
    else:
        return first[mid] # If the date is equal, returns the value of the date and ends the program


def is_earlier(guess = 10):
   return int(input("{}: 1 - earlier, 2 - later, 3 - equal?: ".format(guess))) # Puts the date that the computer has guessed and asks the user
                                                                               # if the date is earlier, later or equal


if __name__ == '__main__':
   print ('Think of a specific date in any year')
   print ('e.g., Jan 1 or Feb 29 or Jul 4 or Dec 25')
   print ('Truthfully answer "Yes" or "No" to the following questions')
   print ('I will determine the date in ten questions or less') # Explains the game to user

   print(guess_game()) 

