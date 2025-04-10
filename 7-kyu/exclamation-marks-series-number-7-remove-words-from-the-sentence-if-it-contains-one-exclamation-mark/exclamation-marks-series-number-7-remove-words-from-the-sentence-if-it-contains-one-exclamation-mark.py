def remove(s):
    str_split = s.split(' ')
    res = []
    for str in str_split:
        if str.count('!') != 1:
            res.append(str)
    return ' '.join(res)
        