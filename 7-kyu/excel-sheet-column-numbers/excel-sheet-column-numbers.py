def title_to_number(title): 
    res = 0
    for letter in title:
        value = ord(letter) - ord('A') + 1
        res = res * 26 + value
    return res