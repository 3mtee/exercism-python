def factors(value):
    results = []
    i = 2
    num = value
    while num != 1:
        if num % i == 0:
            results.append(i)
            num = num / i
        else:
            i += 1
    return results


def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
