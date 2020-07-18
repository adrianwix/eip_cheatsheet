import random


def merge(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c


def sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    mitte = n // 2
    a = sort(arr[0:mitte])
    b = sort(arr[mitte:n])
    c = merge(a, b)
    return c


F = [random.randint(1000, 9999) for i in range(100000)]
