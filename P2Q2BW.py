# Boris Wang
# Assignment 1 - Python Decision Making
# Computer Science 20, blk 3
# February 10, 2021

# This program is my own work - BW

points = input("How many points do you have? ")

if int(points) < 2500:
    print("Sorry, but you do not qualify for a gift card.\n")

elif 2500 <= int(points) < 7500:
    print("You can redeem 2500 points and spend $10 to receive a $15 gift card.")
    spend = input("Would you like to do this (yes or no)? ")
    if spend.lower() == "yes":
        print("\nRedeeming 2500 points from", str(points), "points and $10 for a $15 gift card\n")
        print("You have", int(points) - 2500, "points remaining.")
    elif spend.lower() == "no":
        print("\nYou will qualify for a $15 gift card with", 7500 - int(points), "more points.")
elif 7500 <= int(points) < 10000:
    print("Redeeming 7500 points from", str(points), "points for a $15 gift card.\n ")
    print("You have", int(points) - 7500, "points remaining.")
elif 10000 <= int(points) < 15000:
    print("Redeeming 10000 points from", str(points), "points for a $20 gift card.\n ")
    print("You have", int(points) - 10000, "points remaining.")
elif 15000 <= int(points) < 29999:
    print("Redeeming 15000 points from", str(points), "points for a $25 gift card.\n ")
    print("You have", int(points) - 15000, "points remaining.")
elif 30000 <= int(points) < 50000:
    print("Redeeming 30000 points from", str(points), "points for a $50 gift card.\n ")
    print("As a free gift, you qualify for either:")
    print("-> (a) $5 off your next purchase OR ")
    print("-> (b) $5 donation made to the food bank\n")
    dono = input("Please choose (a) or (b): ")
    if dono.lower() == "a":
        print("You will receive $5 off on your next purchase.\n")
        print("You have", int(points) - 30000, "points remaining.")
    elif dono.lower() == "b":
        print("Thank you for your generous $5 donation!\n")
        print("You have", int(points) - 30000, "points remaining.")
elif int(points) >= 50000:
    print("WOWZA YOU HAVE", str(points),"YOU GET A FREE PURCHASE POG CHAMP")
    print("Redeeming 50000 points from", str(points), "points for a FREE PURCHASE.\n ")
    print("You have", int(points) - 50000, "points remaining.")
