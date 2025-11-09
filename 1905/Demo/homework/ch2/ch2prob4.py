# Problem 4: Simple Calculator
# Perform a basic arithmetic operation based on a choice.

operand1 = 10
operand2 = 5
operation_choice = "add"  # Can be "add", "subtract", "multiply", or "divide"

# if operation_choice == "add":
#     result = operand1 + operand2
#     print("Result of addition:", result)
# elif operation_choice == "subtract":
#     result = operand1 - operand2
#     print("Result of subtraction:", result)
# elif operation_choice == "multiply":
#     result = operand1 * operand2
#     print("Result of multiplication:", result)
# elif operation_choice == "divide":
#     # Check for division by zero
#     if operand2 != 0:
#         result = operand1 / operand2
#         print("Result of division:", result)
#     else:
#         print("Error: Division by zero is not allowed.")
# else:
#     print("Invalid operation choice.")

result = None
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
    case _:
        print("Invalid operation choice.")

if result:
    print("Result of {operation_choise}:", result)
