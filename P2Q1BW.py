# Boris Wang
# Assignment 1 - Python Decision Making
# Computer Science 20, blk 3
# February 10, 2021

# This program is my own work - BW

total = 0
timebathroom = 0
timesupper = 0
timeother = 0
timedishes = 0

print("Weekly chore summary:")

bathroom = input("1. Did you clean the bathroom (yes or no)? ")
if bathroom.lower() == "yes":
    timebathroom = 75
    print(timebathroom, "minutes added\n")
elif bathroom.lower() == "no":
    print("No extra time\n")

supper = input("2. How many times did you make supper? Enter a number: ")
if int(supper) == 0:
    print("No extra time")
elif int(supper) == 1 or int(supper) == 2:
    timesupper = int(supper)* 30
    print(timesupper, "minutes added\n")
elif int(supper) == 3 or int(supper) == 4:
    timesupper = int(supper) * 45
    print(timesupper, "minutes added\n")
elif int(supper) >= 5:
    timesupper = int(supper) * 60
    print(timesupper, "minutes added\n")

other = input("Did you do (a) vacuum, (b) do the laundry, or (c) neither (a, b, c)? ")
if other.lower() == "a":
    basement = input("-> Including the basement (yes or no)? ")
    if basement.lower() == "yes":
        timeother = 60
        print(timeother, "minutes added\n")
    elif basement.lower() == "no":
        timeother = 45
        print(timeother, "minutes added\n")
elif other.lower() == "b":
    timeother = 90
    print(timeother, "minutes added\n")
elif other.lower() == "c":
    print("No extra time\n")
    
dishes = input("Did you do the dishes? (yes or no)? ")
if dishes.lower() == "yes":
    timedishes = 80
    print(timedishes, "minutes added\n")
elif dishes.lower() == "no":
    print("No extra time\n")

total = timesupper + timeother + timebathroom + timedishes
money = total//60*13

if total < 60:
    money = 0
    print("You worked on chores for", str(total), "minutes. You earned $" + str(money), "this week.")
elif money <= 100:
    print("You worked on chores for", str(total), "minutes. You earned $" + str(money), "this week.")
elif money > 100:
    money = 100
    print("You worked on chores for", str(total), "minutes. You earned $" + str(money), "this week.")
