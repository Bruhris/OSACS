def linear_search(arr, length_arr, value):
 
    for i in range(length_arr):
        if (arr[i] == value):
            return i
    return -1

arr = [15, 22, 75, 5, 29, 37, 23, 18, 44, 2, 20, 19, 97, 71, 93, 25, 13, 4, 10, 14, 41, 8, 56 ]
find_value = 22
linear_search(arr, len(arr), find_value)