import heapq
def largest(n, xs):
#     sorted_list = sorted(xs)
#     return sorted_list[-n:]
    return sorted(heapq.nlargest(n, xs))