def is_isogram(string: str):
    clean_string = "".join(c.lower() for c in string if c.isalpha())
    return len(set(clean_string)) == len(clean_string)
