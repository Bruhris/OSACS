# Boris Wang
# Python Demo Q1
# Computer Science 20, blk 3
# February 3, 2021

# This program is my own work - BW

import random

temp = input("What is the temperature today in celsius? ")
convTemp = int(temp) * 9 / 5 + 32
print("That means the temperature is ", convTemp, " in fahrenheit")
check = (random.randint(0, 10))
if check % 2 == 0:
    print("By our calculations, it also seems that it will rain tomorrow!")
else:
    print("By our calculations, it also seems that it will also snow tomorrow!")
