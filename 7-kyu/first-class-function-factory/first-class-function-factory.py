def factory(x):
    def another_fun(arr):
        res = []
        for i, num in enumerate(arr):
            res.append(x * num)
        return res
    return another_fun