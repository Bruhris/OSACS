def bubble_sort(arr):
    n = len(arr)
    for i in range(n): # Goes through the whole array
        for j in range(n-i-1): # -1 is to not compare outside of array and i is for the number of elements already sorted
            if arr[j] > arr[j+1]: # Compares the element next to it and if it is less than j value, will swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    return arr

arr = [89, 2, 71, 37, 11, 59, 97, 83, 5, 47, 13, 67,
       7, 19, 3, 17, 31, 43, 29, 41, 23, 53, 61, 73, 79]

bubble_sort(arr)