from collections import Counter

"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0
    if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        return sum(i for i in dice if i == category)
    if category == FULL_HOUSE:
        counts = Counter(dice)
        return sum(k * v for k, v in counts.items()) if sorted(list(counts.values())) == [2, 3] else 0
    if category == FOUR_OF_A_KIND:
        counts = Counter(dice)
        return sum(k * 4 for k, v in counts.items() if v >= 4)
    if category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
    if category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
    if category == CHOICE:
        return sum(dice)
    return 0
