def slices(series, length):
    series_length = len(series)
    if length > series_length or length < 1:
        raise ValueError("Incorrect length was requested")

    return [series[a:a + length] for a in range(0, series_length - length + 1)]
