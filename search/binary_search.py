def binary_search(arr, target):
    '''
    This is an implementation of the binary search algorithm. If there are duplicate indices for the target value
    it will return any one of those indicies.
    
    Input:
      arr - sorted array to be search
      target - value searching for
    '''
    left_point, right_point = 0, len(arr) - 1
    
    while left_point <= right_point:
        mid = (right_point + left_point) // 2 # mid point
        if arr[mid] == target: # found target
            return mid
        elif arr[mid] > target: # target is in lower half (arr[:mid])
            right_point = mid - 1
        else: # target is in upper half (arr[mid:])
            left_point = mid + 1
    return -1
