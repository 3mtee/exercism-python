def equilateral(sides):
    return __check_side_differences(sides, 1)


def isosceles(sides):
    return __is_triangle_valid(sides) and len(set(sides)) <= 2


def scalene(sides):
    return __check_side_differences(sides, 3)


def __is_triangle_valid(sides):
    if len(sides) != 3:
        return False

    for i, s in enumerate(sides):
        copies = sides.copy()
        side = copies.pop(i)
        if side <= 0:
            return False

        if copies[0] + copies[1] <= side:
            return False

    return 0 not in sides


def __check_side_differences(sides, e_size):
    return __is_triangle_valid(sides) and len(set(sides)) == e_size
