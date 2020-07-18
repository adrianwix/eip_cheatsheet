def f(n):
    if n == 0:
        return 1
    x = f(n - 1)
    return x * n
