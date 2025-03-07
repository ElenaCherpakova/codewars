from itertools import zip_longest 
def transpose_two_strings(arr):
    a, b = arr[0], arr[1]
    t = zip_longest(a, b, fillvalue= ' ')
    # for pair in t:
    #     res.append(' '.join(pair))
    # return '\n'.join(res)
    return '\n'.join(' '.join(pair) for pair in t)
    
    
    # max_len = max(len(a), len(b))
    # a = a.ljust(max_len)
    # b = b.ljust(max_len)
    
    # res = []
    # t = zip(a, b)
    
    # for pair in t:
    #     res.append(' '.join(pair))
    # return '\n'.join(res)

    
