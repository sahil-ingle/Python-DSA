
# It's Not a practical Sorting Method

import random

def bogoSort(a):
    n = len(a)
    while (is_sorted(a) == False):
        shuffle(a)
    return a

def is_sorted(a):
    n = len(a)
    for i in range(0, n - 1):
        if (a[i] > a[i + 1]):
            return False
    return True

def shuffle(a):
    n = len(a)
    for i in range(0, n):
        r = random.randint(0, n - 1)
        a[i], a[r] = a[r], a[i]


a = [3, 2, 4, 1, 0, 5]

print(bogoSort(a))
