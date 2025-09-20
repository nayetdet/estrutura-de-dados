from impl.stack import Stack

def transfer(src, dst):
    while not src.is_empty():
        value = src.pop()
        dst.push(value)

def main():
    s = Stack([1, 2, 3])
    t = Stack([4, 5, 6])
    print(f"s (start): {s.values}")
    print(f"t (start): {t.values}")

    transfer(s, t)
    print(f"s (end): {s.values}")
    print(f"t (end): {t.values}")

if __name__ == "__main__":
    main()
