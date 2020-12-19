from functools import reduce


def classify(number):
    if number < 1:
        raise ValueError("You can't pass number less than 1")
    factors = map(lambda i: i if number % i == 0 else 0, range(1, number))
    aliquot = reduce(lambda x, y: x + y, factors, 0)

    if aliquot == number:
        return "perfect"
    elif aliquot > number:
        return "abundant"
    else:
        return "deficient"
