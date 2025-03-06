def tidyNumber(n):
    asc = int(''.join(sorted(list(str(n)))))
    if asc == n:
        return True
    return False