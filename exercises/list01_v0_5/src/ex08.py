def two_sum(numbers: list[int], target: int, i = 0, j = 1) -> bool:
    if i >= len(numbers):
        return False
    
    if j >= len(numbers):
        return two_sum(numbers, target, i + 1, i + 2)

    if numbers[i] + numbers[j] == target:
        return True

    return two_sum(numbers, target, i, j + 1)
