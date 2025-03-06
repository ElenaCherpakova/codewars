def encode(st):
    res = ''    
    for char in list(st):
        if char.isalpha():
            num = str(ord(char.lower()) - ord('a') + 1)
            res += num
        else:
            res +=char
    return res