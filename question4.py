def sumN(n, total=0):
    if n == 0:
        return total
    return sumN(n - 1, total + n)
