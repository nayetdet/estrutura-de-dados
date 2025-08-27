"""
O(n)
max_element([3, 1, 4])
│
├── a = 3
└── b = max_element([1, 4])
        │
        ├── a = 1
        └── b = max_element([4])
                └── retorna 4
"""
def max_element(numbers: list[int]) -> int | None:
    if len(numbers) == 0:
        return None
    
    if len(numbers) == 1:
        return numbers[0]

    a = numbers[0]
    b = max_element(numbers[1:])
    return a if a > b else b
