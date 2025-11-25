def romanToInt(s: str) -> int:
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev = 0

    for char in reversed(s):

        value = values[char]

        # If a smaller numeral comes before a larger one, subtract it
        if value < prev:
            total -= value
        else:
            total += value

        prev = value

    return total