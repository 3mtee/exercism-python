def saddle_points(matrix):
    if len(set(map(len, matrix))) > 1:
        raise ValueError("Irregular matrices are forbidden")

    rotated_matrix = list(zip(*matrix))
    points = set()
    for i, row in enumerate(matrix):
        for j, x in enumerate(row):
            if x == max(row) and x == min(rotated_matrix[j]):
                points.add((i, j))
    return [{"row": p[0] + 1, "column": p[1] + 1} for p in points]

