def digit_sum(number: int) -> int:
    if number < 10:
        return number
    
    return digit_sum(number // 10) + (number % 10)
