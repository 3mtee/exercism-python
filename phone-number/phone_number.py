import re


class PhoneNumber:
    def __init__(self, number):
        self.number = self.clear_number(number)
        self.area_code = self.number[0:3]
        wrong_length = len(self.number) > 10
        wrong_n = int(self.number[0]) < 2 or int(self.number[3]) < 2
        if wrong_length or wrong_n:
            raise ValueError("Incorrect input")

    def pretty(self):
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}"

    @staticmethod
    def clear_number(number: str):
        parts = re.findall(r"\d+", number)
        num = "".join(parts)
        if len(num) == 11 and num[0] == "1":
            return num[1:]
        return num
