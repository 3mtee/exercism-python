def saddle_points(matrix):
    saddles: list[map] = []

    row_len = None
    for row_num, row in enumerate(matrix):
        saddle = max(row)
        if row_num == 0:
            row_len = len(row)

        if len(row) != row_len:
            raise ValueError("Irregular matrices are forbidden")

        saddles += [{"row": row_num + 1, "column": i + 1, "value": s} for i, s in enumerate(row) if s == saddle]

    for i, saddle in enumerate(saddles.copy()):
        col_num = saddle["column"] - 1
        for row in matrix:
            if row[col_num] < saddle["value"]:
                saddles[i] = None
    return [{"row": s["row"], "column": s["column"]} for s in saddles if s]

