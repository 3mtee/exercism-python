verses = (
    ("first", "a Partridge in a Pear Tree"),
    ("second", "two Turtle Doves, and"),
    ("third", "three French Hens,"),
    ("fourth", "four Calling Birds,"),
    ("fifth", "five Gold Rings,"),
    ("sixth", "six Geese-a-Laying,"),
    ("seventh", "seven Swans-a-Swimming,"),
    ("eighth", "eight Maids-a-Milking,"),
    ("ninth", "nine Ladies Dancing,"),
    ("tenth", "ten Lords-a-Leaping,"),
    ("eleventh", "eleven Pipers Piping,"),
    ("twelfth", "twelve Drummers Drumming,"),
)


def build_line(start_index, end_index):
    loot = " ".join(v[1] for v in (verses[start_index:end_index + 1][::-1]))
    return f"On the {verses[end_index][0]} day of Christmas my true love gave to me: {loot}."


def recite(start_verse, end_verse):
    return [build_line(0, n) for n in range(start_verse - 1, end_verse)]
