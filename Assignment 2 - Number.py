# * ***********************************************************************
# Boris Wang
# Exercise 1 - Leap Year
# Computer Science 30 - Block 6
# September 24, 2021

# This program is my own work - BW

import math # import libraries

# Declare lists for the prime, fibonacci numbers and the data that is being used
prime_nums = []
fibonacci_nums = []
data = [51, 68, 15, 90, 78, 97, 14, 56, 81, 79, 26, 80, 48, 64, 37, 88, 94, 91, 6, 44, 49, 9, 34, 85, 25, 95, 67, 11, 47, 58, 65, 50, 61, 100, 36, 40, 63, 5, 89, 57, 45, 53, 30, 4, 69, 71, 82, 77, 59, 74, 75, 10, 27, 72, 86, 24, 31, 52, 3,
        23, 41, 46, 32, 38, 21, 62, 55, 83, 43, 16, 98, 33, 12, 7, 60, 66, 54, 18, 92, 29, 35, 8, 20, 96, 1, 76, 17, 93, 73, 84]

def sort(arr): # Uses a bubble sort to sort the array given
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return str(arr)[1:-1] # Returns the array as a string, removing the outside brackets

def fibonacci(arr): # Uses an algorithm to determine what numbers of an array are fibonacci numbers
    for num in range(2, len(arr)-1):
        if perfect_square(5*pow(arr[num],2)-4) or perfect_square(5*pow(arr[num],2)+4):
            fibonacci_nums.append(arr[num])


def prime(arr): # Uses an algorithm to determine what numbers of an array are prime numbers
    for num in range(2, len(arr)-1):
        if arr[num] > 1:
            for k in range(2, arr[num]):
                if arr[num] % k == 0:
                    break
            else:
                prime_nums.append(arr[num])

def perfect_square(num): # Checks if number is perfect square
    sqrt_num = int(math.sqrt(num))
    return pow(sqrt_num,2) == num

def main():
    # Prints the data after it is sorted using the sort() function and what data is missing from the list
    print(sort(data))
    print("You are missing the following numbers from the data: ")

    # Adds the missing numbers to a list called nums_missing
    nums_missing = []
    for number in range(101):
        if number not in data:
            print(number, end=' ')
            nums_missing.append(number)
    
    # Asks if the user wants to add the missing numbers from the data or not
    add = input("\nDo you want to add them to the data or leave it be? (A or L) ").lower()
    while add not in 'al': # Error check
        print("That input is invalid")
        add = input("Do you want to add them to the data or leave it be? (A or L) ").lower()
    if add == 'a':
        data.extend(nums_missing)
        sort(data)
    while True:
        # Asks the user if they want to see the prime numbers, fibonacci numbers or if they want to exit the program
        choice = input("Do you want to print the prime numbers of the data, the Fibonacci numbers or do you want to quit? (P or F or E) ").lower()
        while choice not in 'pfe':
            print("That input is invalid")
            choice = input("Do you want to print the prime numbers of the data, the Fibonacci numbers or do you want to quit? (P or F or E) ").lower()
        if choice == 'p':
            prime(data)
            print("Within your data (starting from the third term), there are",len(prime_nums),"prime numbers:")
            print(str(prime_nums)[1:-1])
        elif choice == 'f':
            fibonacci(data)
            print("Within your data (starting from the third term), there are",len(fibonacci_nums),"fibonaccci numbers:")
            print(str(fibonacci_nums)[1:-1])
        else:
            print("Thanks for using my program")
            break

    

if __name__ == "__main__":
    main()