def in_nlist(lst, target):
    if not lst:
        return False
    elif lst[0] == target:
        return True
    elif not isinstance(lst[0], list):
        return in_nlist(lst[1:], target)
    else:
        return in_nlist(lst[0], target) or in_nlist(lst[1:], target)
    
print(in_nlist([[1, 3], 2, [[4]]], 5))