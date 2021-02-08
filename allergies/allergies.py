class Allergies:
    allergens = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128
    }

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        allergen_score = Allergies.allergens[item]
        return self.score & allergen_score != 0

    @property
    def lst(self):
        return [k for k, v in Allergies.allergens.items() if self.allergic_to(k)]
