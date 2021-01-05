import re
import functools
import operator


def is_valid(isbn):
    pattern = re.compile(r"(?:(\d+)(?:-)?(X)?)")
    tup = pattern.findall(isbn)

    refined = "".join([a + b for a, b in tup])
    if len(refined) != 10 or ("X" in refined and refined.index("X") != 9):
        return False
    i = 10
    res = []
    for r in refined:
        n = 10 if r == "X" else int(r)
        res.append(n * i)
        i = i - 1
    return functools.reduce(operator.add, res) % 11 == 0
