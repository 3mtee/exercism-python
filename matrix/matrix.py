class Matrix:
    def __init__(self, matrix_string: str):
        lines = matrix_string.splitlines()
        splitlines_ = [list(map(int, line.split())) for line in lines]
        self.__matrix = splitlines_

    def row(self, index):
        return self.__matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.__matrix]
