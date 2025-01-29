def sum_rec(n):
    if n == 1:
        return n
    else:
        return n + sum_rec(n-1)


sum_rec(10)
