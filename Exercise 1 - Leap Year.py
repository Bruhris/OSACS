# * ***********************************************************************
# Boris Wang
# Exercise 1 - Leap Year
# Computer Science 30 - Block 6
# September 13, 2021

# This program is my own work - BW

user_year = int(input('Input a year: '))

if user_year % 4 == 0:
    if user_year % 100 == 0:
        if user_year % 400 == 0:
            print('That is a leap year')
        else:
            print('That is not a leap year')
    else:
        print('That is a leap year')
else:
    print('That is not a leap year')
