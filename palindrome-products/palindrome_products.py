def smallest(max_factor, min_factor):
    return is_palindrome(min_factor, max_factor)


def largest(max_factor, min_factor):
    return is_palindrome(min_factor, max_factor, low=False)


def is_palindrome(mn, mx, low=True):
    """
    Throughout the method all ranges' upper bound is extended because in python it's exclusive
    and we need to include it.
    :param mn: min value
    :param mx: max value
    :param low: True means we need smallest palindrome, False - largest one
    :return:
    """
    if mn > mx:
        raise ValueError("min shouldn't be bigger than max")
    # iterate over range of squares to avoid nested loops
    args = (mn ** 2, mx ** 2 + 1) if low else (mx ** 2, mn ** 2 - 1, -1)

    for r in range(*args):
        s = str(r)
        palindrome = s == s[::-1]
        if palindrome:
            # Since we're iterating through range created using smallest and largest squares as its bounds,
            # it'll contain numbers which aren't products of the min-max range.
            # So we need to check if there's a factor of a palindrome in the initial range
            # mn <= r // j <= mx is here because we extended our ranges by 1
            factor_in_range = any(mn <= r // j <= mx for j in range(mn, mx + 1) if r % j == 0)
            if factor_in_range:
                # Similar to the above we need to find the factors of a palindrome in the initial range
                return r, ((i, r // i) for i in range(mn, mx + 1)
                           if r % i == 0 and mn <= i <= r // i <= mx)
    else:
        return None, []

