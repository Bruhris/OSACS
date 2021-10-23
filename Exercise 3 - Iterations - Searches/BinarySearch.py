# * ***********************************************************************
# Boris Wang
# Exercise 1 - Leap Year
# Computer Science 30 - Block 6
# October 24, 2021

# This program is my own work - BW


def binarySearch (arr, l, r, x):

    if r >= l: # If the list is not empty
  
        mid = l + (r - l) // 2 # Gets the middle element of the given array

        print("I current checking index",mid,"of the list")

        if arr[mid] == x: # If it finds the value, will return the index value
            print("The index of the value you are looking for in the sorted list, is in index",mid)
            return mid
          
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x) # If the index value is greater than the find_value, then the index must be behind the mid
                                                  # index and will search the lower half of the list
  
        else:
            return binarySearch(arr, mid + 1, r, x) # If the index value is less than the find_value, then the index must be infront of the mid
                                                    # index and will search the upper half of the list
  
    else:
        return -1 # If the value is not in the list, then return -1

arr = [15, 22, 75, 5, 29, 37, 23, 18, 44, 2, 20, 19, 97, 71, 93, 25, 13, 4, 10, 14, 41, 8, 56]
arr.sort()
print(arr)
find_value = 44
binarySearch(arr, 0, len(arr), find_value)
