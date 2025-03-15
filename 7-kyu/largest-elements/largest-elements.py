import heapq
def largest(n, xs):
    # O(m log m)
#     sorted_list = sorted(xs)
#     return sorted_list[-n:]

    # O(m log n) - faster
    return sorted(heapq.nlargest(n, xs))
