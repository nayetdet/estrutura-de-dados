def cut_odds(number: int) -> int:
    digit = number % 10
    cutted_digit = digit if digit % 2 == 1 else 0
    
    if number < 10:
        return cutted_digit

    if cutted_digit == 1:
        return cut_odds(number // 10)
    return 10 * cut_odds(number // 10) + cutted_digit
