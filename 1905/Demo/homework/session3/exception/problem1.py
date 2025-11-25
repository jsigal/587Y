# 1. Write an exception handler for dividing a number than handles ValueError and ZeroDivisionError, 
# using else to display the result and finally to inform when it is completed

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input. Please enter an integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result}")
finally:
    print("Execution complete.")