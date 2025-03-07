def transpose_two_strings(arr):
    a, b = arr[0], arr[1]
    
    max_len = max(len(a), len(b))
    a = a.ljust(max_len)
    b = b.ljust(max_len)
    
    res = []
    t = zip(a, b)
    
    for pair in t:
        res.append(' '.join(pair))
    return '\n'.join(res)