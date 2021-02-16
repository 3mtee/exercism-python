from string import ascii_lowercase
import random

CHAR_POOL = list(ascii_lowercase)


class Cipher:
    def __init__(self, key="".join(random.choices(CHAR_POOL, k=100))):
        self.key = key
        self.key_len = len(self.key)

    def encode(self, text):
        return self.__do_stuff(text, False)

    def decode(self, text):
        return self.__do_stuff(text, True)

    def __do_stuff(self, text, decode):
        text_len = len(text)
        if self.key_len < text_len:
            key_to_use = (self.key * (int(text_len / self.key_len) + 1))[:text_len]
        else:
            key_to_use = self.key
        z = zip(key_to_use[:text_len], list(text))
        return "".join(self.__get_char(c, k, decode) for k, c in z)

    @staticmethod
    def __get_char(char, key_char, reverse):
        if reverse:
            index = CHAR_POOL.index(char) - CHAR_POOL.index(key_char)
        else:
            index = CHAR_POOL.index(char) + CHAR_POOL.index(key_char)
        return CHAR_POOL[index if index < len(CHAR_POOL) else index - len(CHAR_POOL)]
