def is_isogram(string: str):
    clean_string = "".join(c for c in string.lower() if c.isalpha())
    return len(set(clean_string)) == len(clean_string)
