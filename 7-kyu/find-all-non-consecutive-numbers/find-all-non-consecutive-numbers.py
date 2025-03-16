def all_non_consecutive(arr):
    res = []
    
    for i, num in enumerate(arr):
        count = {}
        if i > 0 and arr[i] - arr[i-1] !=1:
            count['i'] = i
            count['n'] = num
            res.append(count)
    return res
​