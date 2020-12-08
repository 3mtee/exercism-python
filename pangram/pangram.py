ABC = set("abcdefghijklmnopqrstuvwxyz")
ABC_LENGTH = len(ABC)



def is_pangram(sentence):
    common = set(sentence.lower()) & ABC
    return len(common) == ABC_LENGTH
