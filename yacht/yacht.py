from collections import Counter

YACHT = (lambda x: 50 if len(set(x)) == 1 else 0)
ONES = (lambda x: __count_dices(x, 1))
TWOS = (lambda x: __count_dices(x, 2))
THREES = (lambda x: __count_dices(x, 3))
FOURS = (lambda x: __count_dices(x, 4))
FIVES = (lambda x: __count_dices(x, 5))
SIXES = (lambda x: __count_dices(x, 6))
FULL_HOUSE = (lambda x: sum(x) if sorted(Counter(x).values()) == [2, 3] else 0)
FOUR_OF_A_KIND = (lambda x: sum(k * 4 for k, v in Counter(x).items() if v >= 4))
LITTLE_STRAIGHT = (lambda x: 30 if sorted(x) == [1, 2, 3, 4, 5] else 0)
BIG_STRAIGHT = (lambda x: 30 if sorted(x) == [2, 3, 4, 5, 6] else 0)
CHOICE = sum


def score(dice, category):
    return category(dice)


def __count_dices(x: list, digit):
    return sum(i for i in x if i == digit)
