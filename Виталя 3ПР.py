def main(p, b, m, n):
    total = 0
    total2 = 0
    for c in range(1, b + 1):
        for k in range(1, n + 1):
            left = 39 * (k - c**2)**7 - p**4 - p**6
            total += total + left
    for k in range(1, n + 1):
        for j in range(1, b + 1):
            for i in range(1, m + 1):
                right = 81 * j**4 - (1 - i / 9 - 8 * k**3)
                total2 += total2 + right
    return total - total2
