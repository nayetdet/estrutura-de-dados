from impl.stack import Stack

def compile(expr):
    instructions = []
    eval_stack = Stack()
    temp_counter = 0

    for element in expr:
        if element in ("+", "-", "*", "/"):
            b = eval_stack.pop()
            a = eval_stack.pop()
            instructions.append(f"LD {a}")

            match element:
                case "+": instructions.append(f"AD {b}")
                case "-": instructions.append(f"SB {b}")
                case "*": instructions.append(f"ML {b}")
                case "/": instructions.append(f"DV {b}")
            
            temp = f"TEMP{temp_counter + 1}"
            temp_counter += 1

            instructions.append(f"ST {temp}")
            eval_stack.push(temp)
        else: eval_stack.push(element)
    return instructions

def main():
    # [(A + B*C) / (D - E)]
    postfix_expression = "ABC*+DE-/"
    instructions = compile(postfix_expression)
    print("\n".join(instructions))

if __name__ == "__main__":
    main()
