def lucky_sum(a, b, c):
    for num in (a, b, c):
        if num == 13:
            return sum(x for x in (a, b, c)[:(a, b, c).index(13)])
    return a + b + c