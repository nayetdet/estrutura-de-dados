def cut_evens(number: int) -> int:
    digit = number % 10
    cutted_digit = digit if digit % 2 == 1 else 0
    
    if number < 10:
        return cutted_digit

    if cutted_digit == 0:
        return cut_evens(number // 10)
    return 10 * cut_evens(number // 10) + cutted_digit
