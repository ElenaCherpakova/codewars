def give_change(amount): 
    denoms = [1, 5, 10, 20, 50, 100]
    res = [0] * len(denoms)
    for i in range(5, -1, -1):
        res[i] = amount // denoms[i]
        amount %= denoms[i]
    return tuple(res)