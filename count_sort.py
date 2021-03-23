def count_sort(arr, k):
    '''
    This is a non-negative implementation of count sort it runs with the following
    complexities:
        time - O(K+N)
        space - O(K+N)
    
    Input:
        arr - array to be sorted
        k - integer space to allot to the temp storage array. 
            It is recommeneded to make this an integer for which
            len(arr) < k.
    Output:
        sorted_arr - sorted array
    '''
    
    sorted_arr = [None]*len(arr)
    temp_storage = [0]*(k+1)

    # build array of counts
    for index in range(len(arr)):
        temp_storage[arr[index]] += 1

    # update to number of elements below
    for index in range(1, k+1):
        temp_storage[index] += temp_storage[index-1] 

    for index in range(len(arr)-1, -1, -1):
        sorted_arr[temp_storage[arr[index]]-1] = arr[index]
        temp_storage[arr[index]] -= 1
        
    return sorted_arr
