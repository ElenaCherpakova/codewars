def calculator(txt):
    first, operator, second = txt.split()
    len1, len2 = len(first), len(second)
    if operator == '+':
        return first + second
    if operator == '-':
        return '.' * (len1 - len2)
    if operator == '*':
        return '.' * (len1 * len2)
    if operator == '//':
        return '.' * (len1 // len2)
    