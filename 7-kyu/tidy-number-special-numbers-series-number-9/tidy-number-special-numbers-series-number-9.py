def tidyNumber(n):
#     return n == int(''.join(sorted(list(str(n)))))
​
      s = list(str(n))
      return s == sorted(s)