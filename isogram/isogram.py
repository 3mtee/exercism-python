import re


def is_isogram(string: str):
    clean_string = re.sub("[^a-z]", "", string.lower())
    return len(set(clean_string)) == len(clean_string)
