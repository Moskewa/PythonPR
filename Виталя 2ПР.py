import math


def main(y):
    if y < 155:
        return (61 * y**3 +70)**6 / 2 + 45 * y**2 / 41 + 61 * math.cos(y)**4
    if 155 <= y < 188:
        return (y**3 / 36 - y)**4
    if 188 <= y < 245:
        return 82 * y**5 + 1
    return 30 + y**5
print(main(229))