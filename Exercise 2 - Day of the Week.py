# * ***********************************************************************
# Boris Wang
# Exercise 1 - Leap Year
# Computer Science 30 - Block 6
# September 13, 2021

# This program is my own work - BW

days = ['monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday', 'sunday']

current_day = input('What day of the week is it right now? ')
wait_time = int(input('In how many days do you leave for your holiday? '))

day_number = days.index(current_day.lower()) + 1

day_leave = (day_number + wait_time) % 7 - 1

print('You leave on', days[day_leave])
