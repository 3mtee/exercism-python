PLING = "Pling"
PLANG = "Plang"
PLONG = "Plong"


def convert(number):
    result = ""
    if number % 3 == 0:
        result += PLING
    if number % 5 == 0:
        result += PLANG
    if number % 7 == 0:
        result += PLONG
    if len(result) == 0:
        result = str(number)

    return result
