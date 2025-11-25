# 3. Handle multiple types of exceptions such as FileNotFoundError, ValueError, and ZeroDivisionError

try:
    data = open("nonexistent_file.txt", "r").read()
    result = 10 / int(data)
except FileNotFoundError:
    print("Error: The file could not be found.")
except ValueError:
    print("Error: The file contains non-numeric data.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")