# * ***********************************************************************
# Boris Wang
# Exercise 1 - Leap Year
# Computer Science 30 - Block 6
# September 24, 2021

# This program is my own work - BW

import math

prime_nums = []
fibonacci_nums = []
data = [51, 68, 15, 90, 78, 97, 14, 56, 81, 79, 26, 80, 48, 64, 37, 88, 94, 91, 6, 44, 49, 9, 34, 85, 25, 95, 67, 11, 47, 58, 65, 50, 61, 100, 36, 40, 63, 5, 89, 57, 45, 53, 30, 4, 69, 71, 82, 77, 59, 74, 75, 10, 27, 72, 86, 24, 31, 52, 3,
        23, 41, 46, 32, 38, 21, 62, 55, 83, 43, 16, 98, 33, 12, 7, 60, 66, 54, 18, 92, 29, 35, 8, 20, 96, 1, 76, 17, 93, 73, 84 ]

def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

def fibonacci(arr):
    for num in range(2, len(arr)-1):
        if perfect_square(5*pow(num,2)-4) or perfect_square(5*pow(num,2)+4):
            fibonacci_nums.append(num)



def prime(arr):
    for num in range(2, len(arr)-1):
        if num > 1:
            for k in range(2, num//2):
                if num % k == 0:
                    break
                else:
                    prime_nums.append(num)
                    break

def perfect_square(num):
    sqrt_num = int(math.sqrt(num))
    return pow(sqrt_num,2) == num

def main():
    print(sort(data))
    print("You are missing these numbers from the data: ")

    for number in range(101):
        if number not in data:
            print(number)
            


main()