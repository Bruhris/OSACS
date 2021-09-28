def selection_sort(arr):
    for i in range(len(arr)): # Goes through the whole array
        min_idx = i           # Assigns the index value of beginning of sorted array
        for j in range(i+1, len(arr)): # Looks at the unsorted subarray
            if arr[min_idx] > arr[j]: # If there is a element in unsorted subarray that is less than the beginning of the sorted subarray
                min_idx = j           # Assign the lower value index as the minimum index
     
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # Swaps the beginning of sorted array with the next smallest value
        print("Iteration", str(i+1)+":", arr)

arr = [89, 2, 71, 37, 11, 59, 97, 83, 5, 47, 13, 67,
       7, 19, 3, 17, 31, 43, 29, 41, 23, 53, 61, 73, 79]

selection_sort(arr)