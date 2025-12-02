# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.


class Calculator:
    """
    Docstring for Calculator
    A class called Calculator to perform basic arithmetic operations
    """
    @staticmethod
    def add(x, y):
        """
        Docstring for add
        A method for addition that takes two arguments and returns their sum
        
        :param x: Operand 1
        :param y: Operand 2
        """
        return x + y

    @staticmethod
    def subtract(x, y):
        """
        Docstring for subtract
        A method for subtraction that takes two arguments and returns their sum
        
        :param x: Operand 1
        :param y: Operand 2
        """
        return x - y

    @staticmethod
    def multiply(x, y):
        """
        Docstring for multiply
        A method for myltiplication that takes two arguments and returns their sum
        
        :param x: Operand 1
        :param y: Operand 2
        """
        return x * y

    @staticmethod
    def divide(x, y):
        """
        Docstring for divide
        A method for division that takes two arguments and returns their sum
        
        :param x: Operand 1
        :param y: Operand 2
        """
        if y != 0:
            return x / y
        else:
            return ("Cannot divide by zero.")

# Perform addition and print the result
result = Calculator.add(7, 5)
print("7 + 5 =", result)

# Perform subtraction and print the result
result = Calculator.subtract(34, 21)
print("34 - 21 =", result)

# Perform multiplication and print the result
result = Calculator.multiply(54, 2)
print("54 * 2 =", result)

# Perform division and print the result
result = Calculator.divide(144, 2)
print("144 / 2 =", result)

# Attempt to perform division by zero, which raises an error, and print the error message
result = Calculator.divide(45, 0)
print("45 / 0 =", result)
