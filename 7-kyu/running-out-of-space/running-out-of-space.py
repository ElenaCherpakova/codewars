from itertools import accumulate
def spacey(array):
    # res = []
    # a = ''  
    # for word in array:
    #     a += word
    #     res.append(a)
    # return res
    return list(accumulate(array))
