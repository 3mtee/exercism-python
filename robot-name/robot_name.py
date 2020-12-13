from string import ascii_uppercase
from string import digits
import random


class Robot:
    previous_names = []

    def __init__(self):
        self.name = None
        self.reset()

    def reset(self):
        robot_name = self.__make_name()
        while robot_name in Robot.previous_names:
            robot_name = self.__make_name()

        Robot.previous_names.append(robot_name)
        self.name = robot_name

    @staticmethod
    def __make_name():
        name_as_list = random.choices(ascii_uppercase, k=2) + random.choices(digits, k=3)
        return "".join(name_as_list)
