import re


def check_isbn_formula(digits):
    numbers_to_mult = list(map(int, digits))
    return sum([factors[0] * factors[1] for factors in zip(numbers_to_mult, range(10, 0, -1))]) % 11 == 0


def is_valid(isbn):
    stripped_isbn = isbn.replace("-", "")
    if not re.compile("[0-9]{9}([0-9]|X)$").match(stripped_isbn):
        return False
    else:
        digits = list(stripped_isbn)
        if digits[-1] == 'X':
            digits[-1] = '10'
        return check_isbn_formula(digits)
