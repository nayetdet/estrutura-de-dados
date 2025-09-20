from impl.stack import Stack

def revert(arr):
    stack = Stack()
    for value in arr:
        stack.push(value)

    arr.clear()
    while not stack.is_empty():
        value = stack.pop()
        arr.append(value)

    return arr

def main():
    arr = [1, 2, 3, 4]
    print(f"arr (start): {arr}")
    print(f"arr (end): {revert(arr)}")

if __name__ == "__main__":
    main()
