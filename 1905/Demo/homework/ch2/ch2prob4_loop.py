# Problem 4: Simple Calculator
# Perform a basic arithmetic operation based on a choice.


while True: 
    result = None
    operand1 = float(input("What is operand1?"))
    operand2 = float(input("What is operand2?"))
    operation_choice = input("What operation? (add, subtract, multiply, divide, quit)")
    match operation_choice:
        case "add":
            result = operand1 + operand2
        case "subtract":
            result = operand1 - operand2
        case "multiply":
            result = operand1 * operand2
        case "divide":
            # Check for division by zero
            if operand2 != 0:
                result = operand1 / operand2
            else:
                print("Error: Division by zero is not allowed.")
        case 'quit':
            break
        case _:
            print("Invalid operation choice.")

    if result:
        print("Result of {operation_choise}:", result)
