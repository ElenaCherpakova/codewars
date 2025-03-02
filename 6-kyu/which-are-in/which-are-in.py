def in_array(array1, array2):
#     res = set()
#     for word_one in array1:
#             for word_two in array2:
#                 if word_one in word_two:
#                     res.add(word_one)
#     return sorted(list(res))
​
      full_str = ' '.join(array2)
      res = { word for word in array1 if word in full_str }
      return sorted(res)