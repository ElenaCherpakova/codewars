def solution(start, finish):  
#     current_position, jumps = start, 0
#     while current_position < finish:
#         if finish - current_position >= 3:
#             step = 3
#         else:
#             step = 1
#         current_position += step
#         jumps += 1
#     return jumps
    distance = finish - start
    three_shelves = distance // 3
    one_shelve = distance % 3
    total_jumps = three_shelves + one_shelve
    return total_jumps
    
    
​
​
            
          