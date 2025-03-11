def solution(start, finish):   
    # jumps = 0
    # while start < finish:
    #     if start + 3 <= finish:
    #         start += 3
    #     else:
    #         start += 1
    #     jumps += 1
    # return jumps
    
    distance = finish - start
    three_shelves = distance // 3
    one_shelve = distance % 3
    total_jumps = three_shelves + one_shelve
    return total_jumps
    
    
​
​
            
          
