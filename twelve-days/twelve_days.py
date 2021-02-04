class Verse:
    def __init__(self, day: str, verse: str):
        self.day = day
        self.verse = verse


verses = (
    Verse("first", "a Partridge in a Pear Tree"),
    Verse("second", "two Turtle Doves, and"),
    Verse("third", "three French Hens,"),
    Verse("fourth", "four Calling Birds,"),
    Verse("fifth", "five Gold Rings,"),
    Verse("sixth", "six Geese-a-Laying,"),
    Verse("seventh", "seven Swans-a-Swimming,"),
    Verse("eighth", "eight Maids-a-Milking,"),
    Verse("ninth", "nine Ladies Dancing,"),
    Verse("tenth", "ten Lords-a-Leaping,"),
    Verse("eleventh", "eleven Pipers Piping,"),
    Verse("twelfth", "twelve Drummers Drumming,"),
)


def build_line(start_index, end_index):
    loot = " ".join(v.verse for v in (verses[start_index:end_index + 1][::-1]))
    return f"On the {verses[end_index].day} day of Christmas my true love gave to me: {loot}."


def recite(start_verse, end_verse):
    return [build_line(0, n) for n in range(start_verse - 1, end_verse)]
