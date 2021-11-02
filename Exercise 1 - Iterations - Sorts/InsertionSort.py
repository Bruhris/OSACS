# * ***********************************************************************
# Boris Wang
# Exercise 1 - Iterations - Sorts
# Computer Science 30 - Block 6
# September 25, 2021

# This program is my own work - BW

def insertion_sort(arr):
    for i in range(1, len(arr)): # Divides the array into sorted and unsorted (Leave atleast one element in array in beginning)
        key = arr[i] # Assigns the beginning of sorted subarray as key
        j = i-1 # Assigns the element index before the key
        while j >= 0 and key < arr[j]: # Checks if there are no elements before the key and the key is less than the element before it
            arr[j + 1] = arr[j] # If so, replace lesser element with greater element
            j -= 1 # Reduces the value of j to compare to elements before and continues till it gets to last element or the element is in the correct spot
        arr[j + 1] = key # Replaces the key value in the correct position after new element is sorted in
        print("Iteration", str(i+1)+":", arr)
    return arr

arr = [89, 2, 71, 37, 11, 59, 97, 83, 5, 47, 13, 67,
       7, 19, 3, 17, 31, 43, 29, 41, 23, 53, 61, 73, 79]

insertion_sort(arr)