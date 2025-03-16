def char_to_ascii(s):
    if len(s) <= 0:
        return None
    res = {}
    full_uniq_string = set(''.join(s.split()))
    for char in full_uniq_string:
        if char.isalpha():
            res[char] = ord(char)
    return res