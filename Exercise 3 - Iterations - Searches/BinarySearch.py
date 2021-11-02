# * ***********************************************************************
# Boris Wang
# Exercise 3 - Iterations - Searches
# Computer Science 30 - Block 6
# October 24, 2021

# This program is my own work - BW


def binarySearch (arr, low, high, x):

    if high >= low: # If the list is not empty
  
        mid = (high + low) // 2 # Gets the middle element of the given array

        print("I current checking index",mid,"of the list","which is the value",arr[mid])

        if arr[mid] == x: # If it finds the value, will return the index value
            print("The index of the value you are looking for in the sorted list, is in index",mid)
            return mid
          
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x) # If the index value is greater than the find_value, then the index must be behind the mid
                                                  # index and will search the lower half of the list
  
        else:
            return binarySearch(arr, mid + 1, high, x) # If the index value is less than the find_value, then the index must be infront of the mid
                                                    # index and will search the upper half of the list
  
    else:
        return -1 # If the value is not in the list, then return -1


arr = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
arr.sort()
print(arr)
find_value = 5
binarySearch(arr, 0, len(arr)-1, find_value)
