from functools import reduce


def classify(number):
    if number < 1:
        raise ValueError("You can't pass number less than 1")
    factors = get_factors(number)
    aliquot = reduce(lambda x, y: x + y, factors, 0)

    if aliquot == number:
        return "perfect"
    elif aliquot > number:
        return "abundant"
    else:
        return "deficient"


def get_factors(number):
    factors = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    return factors
