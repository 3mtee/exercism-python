from string import ascii_lowercase

ABC = set(ascii_lowercase)
ABC_LENGTH = len(ascii_lowercase)


def is_pangram(sentence):
    common = set(sentence.lower()) & ABC
    return len(common) == ABC_LENGTH
