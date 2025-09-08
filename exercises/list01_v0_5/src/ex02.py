def tower_of_hanoi(n: int, src: str, aux: str, dest: str) -> None:
    if n == 1:
        print(f"Mova o disco 1 de {src} para {dest}")
        return

    tower_of_hanoi(n - 1, src, dest, aux)
    print(f"Mova o disco {n} de {src} para {dest}")
    tower_of_hanoi(n - 1, aux, src, dest)
