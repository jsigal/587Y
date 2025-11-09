# Problem 4: Simple Calculator
# Perform a basic arithmetic operation based on a choice.

oper_func = {"add":lambda x,y : x+y,
             "subtract":lambda x,y : x-y,
             "multiply":lambda x,y : x*y,
             "divide":lambda x,y : x/y}

while True: 
    result = None
    operand1 = float(input("What is operand1?"))
    operand2 = float(input("What is operand2?"))
    operation_choice = input("What operation? (add, subtract, multiply, divide, quit)")

    match operation_choice:
        case "add" | "subtract" | "multiply":
            result = oper_func[operation_choice](operand1,operand2)
        case "divide":
            # Check for division by zero
            if operand2 != 0:
                result = oper_func[operation_choice](operand1,operand2)
            else:
                print("Error: Division by zero is not allowed.")
        case 'quit':
            break
        case _:
            print("Invalid operation choice.")

    if result:
        print("Result of {operation_choise}:", result)
