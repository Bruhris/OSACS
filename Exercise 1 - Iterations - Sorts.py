arr = [89, 2, 71, 37, 11, 59, 97, 83, 5, 47, 13, 67,
       7, 19, 3, 17, 31, 43, 29, 41, 23, 53, 61, 73, 79]


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        for k in range(i+1, n):
            if arr[k] < arr[i]:
                arr[i], arr[k] = arr[k], arr[i]

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
