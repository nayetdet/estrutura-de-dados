def odds_zeroed(number: int) -> int:
    digit = number % 10
    zeroed_digit = digit if digit % 2 == 0 else 0

    if number < 10:
        return zeroed_digit

    return 10 * odds_zeroed(number // 10) + zeroed_digit
