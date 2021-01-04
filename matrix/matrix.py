class Matrix:
    def __init__(self, matrix_string: str):
        lines = matrix_string.splitlines()
        self.__matrix = [list(map(int, line.split())) for line in lines]

    def row(self, index):
        return self.__matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.__matrix]
