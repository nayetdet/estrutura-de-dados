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
def sort_by_parity(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers

    a = numbers[0]
    b = sort_by_parity(numbers[1:])
    return [a] + b if a % 2 == 0 else b + [a]
