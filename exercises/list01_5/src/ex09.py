def reorganize_array(numbers: list[int], k: int) -> list[int]:
    if len(numbers) <= 1:
        return numbers
    
    a = numbers[0]
    b = reorganize_array(numbers[:1], k)
    return [a] + b if a <= k else b + [a]
