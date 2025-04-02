from collections import Counter
​
def find_uniq(arr):
    count_char = Counter(frozenset(char.lower()) for char in arr)
#     print(f'count_char {count_char}')
         
    for char in arr:
        char_set = frozenset(char.lower())
#         print(f'count_char {char_set}')
        if count_char[char_set] == 1:
            return char