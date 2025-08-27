def binary_search(numbers: list[int], target: int, low: int = 0, high: int | None = None) -> int | None:
    if high is None:
        high = len(numbers) - 1
    
    if low > high:
        return None

    mid = (low + high) // 2
    if numbers[mid] == target:
        return mid

    if numbers[mid] < target: low = mid + 1
    else: high = mid -1
    return binary_search(numbers, target, low, high)
