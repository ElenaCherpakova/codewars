def sum_even_numbers(seq): 
   # even_list =  []
   # for num in seq:
   #  if num % 2 == 0:
   #      even_list.append(num)
   # return sum(even_list)
   return sum(filter(lambda x: x % 2==0, seq))
