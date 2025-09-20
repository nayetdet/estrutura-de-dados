from impl.stack import Stack

class PStack(Stack):
    def ppush(self, value):
        self.push(value)
        print(f"push({value}): {self.items}")

    def ppop(self):
        self.pop()
        print(f"pop(): {self.items}")

def main():
    stack = PStack()
    stack.ppush(5)
    stack.ppush(3)
    stack.ppop()
    stack.ppush(5)
    stack.ppush(8)
    stack.ppop()
    stack.ppop()
    stack.ppush(9)
    stack.ppush(1)
    stack.ppush(1)
    stack.ppop()
    stack.ppush(7)
    stack.ppush(6)
    stack.ppop()
    stack.ppop()
    stack.ppush(4)
    stack.ppop()
    stack.ppop()

if __name__ == "__main__":
    main()
