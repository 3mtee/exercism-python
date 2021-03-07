def sum_of_multiples(limit, multiples):
    if len(multiples) == 0:
        return 0
    return sum(num for num in range(min(multiples), limit) if
               any(m != 0 and num % m == 0 for m in multiples))
