import re


class PhoneNumber:
    _pattern = re.compile(r"""
           ^\+?1?                   #country
           [-. (]*([2-9]\d{2})\)?   #area
           [-. (]*([2-9]\d{2})\)?   #exchange
           [-. (]*(\d{4})\)?$       #subscriber
           """, re.VERBOSE)

    def __init__(self, number):
        try:
            self.area_code, self.exchange, self.subscriber = self._pattern.search(number.strip()).groups()
        except AttributeError:
            raise ValueError("Invalid input")

    @property
    def number(self):
        return self.area_code + self.exchange + self.subscriber

    def pretty(self):
        return f"({self.area_code})-{self.exchange}-{self.subscriber}"
