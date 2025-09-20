from impl.stack import Stack

def pop_all(stack):
    if stack.is_empty():
        return

    stack.pop()
    pop_all(stack)

def main():
    stack = Stack([1, 2, 3])
    print(f"stack (start): {stack.values}")
    pop_all(stack)
    print(f"stack (end): {stack.values}")

if __name__ == "__main__":
    main()
