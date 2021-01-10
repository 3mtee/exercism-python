def response(hey_bob: str):
    string = hey_bob.strip()
    if string.isupper():
        if string[-1] == "?":
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif not string:
        return "Fine. Be that way!"
    elif string[-1] == "?":
        return "Sure."
    else:
        return "Whatever."
