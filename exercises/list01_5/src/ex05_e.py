def evens_zeroed(number: int) -> int:
    digit = number % 10
    zeroed_digit = digit if digit % 2 == 1 else 0

    if number < 10:
        return zeroed_digit

    return 10 * evens_zeroed(number // 10) + zeroed_digit
