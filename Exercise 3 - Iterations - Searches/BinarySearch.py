def binarySearch (arr, l, r, x):
  
    # Check base case
    if r >= l:
  
        mid = l + (r - l) // 2
  
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
          
        # If element is smaller than mid, then it 
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
  
        # Else the element can only be present 
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
  
    else:
        # Element is not present in the array
        return -1

arr = [15, 22, 75, 5, 29, 37, 23, 18, 44, 2, 20, 19, 97, 71, 93, 25, 13, 4, 10, 14, 41, 8, 56]
find_value = 44
binarySearch(arr, 0, len(arr), find_value)
