def find_uniq(arr):
    unique_num = set(arr)
    a, b = unique_num
    first_three_elem = arr[0:3]
    if first_three_elem.count(a) > 1:
        return b
    else:
        return a
        