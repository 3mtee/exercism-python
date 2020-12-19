def is_armstrong_number(number):
    digits = [int(i) for i in str(number)]
    d_len = len(digits)
    d_sum = 0
    for digit in digits:
        d_sum += digit ** d_len
    return d_sum == number
