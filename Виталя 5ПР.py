import math


def main(y, x):
    n = len(y)
    y.insert(0, 0)
    x.insert(0, 0)
    total = 0
    for i in range(1, n + 1):
        left = 81 * x[n + 1 - i]**2
        right = 50 * y[i]
        total += (left + right)** 7
    return 8 * total