def steps(number):
    if number <= 0:
        raise ValueError("Number should be a positive one")
    return __calc_steps(number, 0)


def __calc_steps(number, step):
    if number == 1:
        return step
    if number % 2 == 0:
        return __calc_steps(number / 2, step + 1)
    else:
        return __calc_steps(number * 3 + 1, step + 1)
