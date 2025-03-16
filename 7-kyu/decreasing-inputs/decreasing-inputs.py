def add(*args):
    res = 0
    for i, num in enumerate(args):
        idx = i + 1
        res += num/idx
    return round(res)
        