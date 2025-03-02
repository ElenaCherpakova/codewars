def delete_nth(order,max_e):
    res = []
    count = {}
    for num in order:
        if count.get(num, 0) < max_e:
            res.append(num)
            count[num] = count.get(num, 0) + 1
    return res