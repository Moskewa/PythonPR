import math


def main(y, x):
    a = math.sqrt(32 * (21 * x**2 + 74 * x**3)**2 + math.exp(1 - 17 * y**3 - 68 * x)**5)
    b = x**2 / 40
    c = (56 * y**2 - 26)**6
    return a + b + c

print(main(0.78, -0.12))