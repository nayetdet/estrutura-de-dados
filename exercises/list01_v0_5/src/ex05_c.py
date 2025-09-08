def digit_length(number: int) -> int:
    if number < 10:
        return 1

    return digit_length(number // 10) + 1
