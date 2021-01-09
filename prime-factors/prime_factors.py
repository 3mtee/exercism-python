def factors(value):
    res = []
    factor = 2
    while value > 1:
        while value % factor == 0:
            res.append(factor)
            value /= factor

        factor += 1
    return res

