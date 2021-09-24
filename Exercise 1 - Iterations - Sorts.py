arr = [89, 2, 71, 37, 11, 59, 97, 83, 5, 47, 13, 67,
       7, 19, 3, 17, 31, 43, 29, 41, 23, 53, 61, 73, 79]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n): # Goes through the whole array
        for j in range(n-i-1): # -1 is to not compare outside of array and i is for the number of elements already sorted
            if arr[j] > arr[j+1]: # Compares the element next to it and if it is less than j value, will swap
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


def selection_sort(arr):
    for i in range(len(arr)): # Goes through the whole array and assigns the 
        min_idx = i # Assigns the index value of loop as the element to compare to other elements
        for j in range(i+1, len(arr)): # Looks at all elements above the element
            if arr[min_idx] > arr[j]: # Compares them and if it is greater than the element being compared (min_idx), changes index value
                min_idx = j           # with the index of the lesser element
     
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # Swaps the first index with the min index


def insertion_sort(arr):
    for i in range(1, len(arr)): # Goes through the second element through the rest of the array
        key = arr[i] # Assigns a value to the loop element of the array
        j = i-1 # Assigns a value to the values less than the index
        while j >= 0 and key < arr[j]: # Checks if there are no elements before the key and the key is less than the element before it
            arr[j + 1] = arr[j] # If so, replace lesser element with greater element
            j -= 1 # Reduces the value of j to compare to elements before and continues till it gets to last element is greater than element before
        arr[j + 1] = key # Replaces the corresponding index value with the key
    return arr

print(insertion_sort(arr))