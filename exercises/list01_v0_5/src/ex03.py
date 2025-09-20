def sort_by_parity(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers

    a = numbers[0]
    b = sort_by_parity(numbers[1:])
    return [a] + b if a % 2 == 0 else b + [a]
