def zero(items, left, right):
    if items[0] == 1997:
        return left
    if items[0] == 1994:
        return right


def one(items, left, middle, right):
    if items[1] == 2017:
        return left
    if items[1] == 2015:
        return middle
    if items[1] == 1964:
        return right


def two(items, left, right):
    if items[2] == 'MUPAD':
        return left
    if items[2] == 'SQL':
        return right


def three(items, left, middle, right):
    if items[3] == 'SQL':
        return left
    if items[3] == 'LATTE':
        return middle
    if items[3] == 'J':
        return right


def main(items):
    return one(
        items,
        zero(items, two(items,0,1),two(items,2,3)),
        two(items,4,5),
        three(items, two(items, 6, 7), zero(items, 8, 9) ,10)
    )
