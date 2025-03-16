def add(*args):
    res = 0
    for i, num in enumerate(args, 1):
        res += num/i
    return round(res)