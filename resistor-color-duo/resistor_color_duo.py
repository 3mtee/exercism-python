_colors = (
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
)


def value(colors):
    return int("".join(str(_colors.index(c)) for c in colors[:2]))
