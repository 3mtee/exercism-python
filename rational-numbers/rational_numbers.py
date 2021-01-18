from math import gcd


class Rational:
    def __init__(self, numer, denom):
        com_div = gcd(numer, denom)
        if denom < 0:
            numer *= -1
            denom *= -1
        self.numer = numer // com_div
        self.denom = denom // com_div

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        new_numer = self.numer * other.denom + other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __sub__(self, other):
        new_numer = self.numer * other.denom - other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        return Rational(numer, denom)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        numer = self.numer ** power
        denom = self.denom ** power
        return Rational(numer, denom)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
