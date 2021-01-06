def largest(min_factor: int, max_factor: int):
    if min_factor > max_factor:
        raise ValueError("min shouldn't be bigger than max")
    value = None
    factors = set()
    for i in range(max_factor, min_factor - 1, -1):
        for j in range(max_factor, min_factor - 1, -1):
            multiplication = i * j
            palindrome = is_palindrome(multiplication)
            if palindrome and (not value or multiplication > value):
                value = multiplication
                factors.clear()
            if multiplication == value:
                factors.add((i, j))
    return value, factors


def smallest(min_factor: int, max_factor: int):
    if min_factor > max_factor:
        raise ValueError("min shouldn't be bigger than max")
    value = None
    factors = set()
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1):
            multiplication = i * j
            palindrome = is_palindrome(multiplication)
            if palindrome and (not value or multiplication < value):
                value = multiplication
                factors.clear()
            if multiplication == value:
                factors.add((i, j))
    return value, factors


def is_palindrome(number: int):
    return str(number)[::-1] == str(number)
