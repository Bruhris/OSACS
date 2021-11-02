# * ***********************************************************************
# Boris Wang
# Exercise 3 - Iterations - Searches
# Computer Science 30 - Block 6
# October 14, 2021

# This program is my own work - BW


def linear_search(arr, length_arr, value):
 
    for i in range(length_arr): # Goes through the whole list and checks if value is in list
        print("I am current searching index",i,"whose value is",arr[i])
        if (arr[i] == value): # If it finds value, return the index value within the list
            print("The value,",value,"you are searching for is located at index",i) 
            return i
    return -1

arr = [15, 22, 75, 5, 29, 37, 23, 18, 44, 2, 20, 19, 97, 71, 93, 25, 13, 4, 10, 14, 41, 8, 56 ]
find_value = 22
linear_search(arr, len(arr), find_value)