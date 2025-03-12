def between_extremes(numbers):
# O(n log n)         
#     s = sorted(numbers)
#     return  s[-1] - s[0]
​
# O(n)
      min = max = numbers[0] 
      for num in numbers[1:]:
        if num < min:
            min = num
        if num > max:
            max = num
      return max - min