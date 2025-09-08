def reversed_number(number: int, result: int = 0) -> int:
    if number == 0:
        return result
    
    digit = number % 10
    return reversed_number(number // 10, 10 * result + digit)
