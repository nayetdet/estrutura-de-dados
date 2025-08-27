def min_digit(number: int) -> int:
    if number < 10:
        return number

    a = number % 10
    b = min_digit(number // 10)
    return a if a < b else b
