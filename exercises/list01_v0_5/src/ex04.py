"""
binary_search([4,10,12,32,34,35,43,76], low=0, high=7)
 └── mid=3 → S[3]=32
     └── 4 < 32 → busca esquerda

        binary_search([4,10,12], low=0, high=2)
         └── mid=1 → S[1]=10
             └── 4 < 10 → busca esquerda

                binary_search([4], low=0, high=0)
                 └── mid=0 → S[0]=4
                     └── ENCONTRADO
"""
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
