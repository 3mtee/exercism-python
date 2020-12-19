def classify(number):
    if number < 1:
        raise ValueError("You can't pass number less than 1")
    aliquot = sum([i for i in range(1, number) if number % i == 0])

    if aliquot == number:
        return "perfect"
    elif aliquot > number:
        return "abundant"
    else:
        return "deficient"
