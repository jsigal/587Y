# 2.	Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
class Calculator:
    """A class to represent a calculator with basic arithmetic operations."""
    
    def __init__(self):
        """Initialize a Calculator object."""
        pass
    
    def add(self, a, b):
        """
        Add two numbers.
        
        Args:
            a (float): The first number
            b (float): The second number
        
        Returns:
            float: The sum of a and b
        """
        return a + b
    
    def subtract(self, a, b):
        """
        Subtract the second number from the first number.
        
        Args:
            a (float): The first number (minuend)
            b (float): The second number (subtrahend)
        
        Returns:
            float: The difference of a and b (a - b)
        """
        return a - b
    
    def multiply(self, a, b):
        """
        Multiply two numbers.
        
        Args:
            a (float): The first number
            b (float): The second number
        
        Returns:
            float: The product of a and b
        """
        return a * b
    
    def divide(self, a, b):
        """
        Divide the first number by the second number.
        
        Args:
            a (float): The first number (dividend)
            b (float): The second number (divisor)
        
        Returns:
            float: The quotient of a and b (a / b)
        
        Raises:
            ZeroDivisionError: If b is zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


# Test the implementation
if __name__ == '__main__':
    calc = Calculator()
    
    # Test case 1: Addition
    print("Test 1: Addition")
    result1 = calc.add(10, 5)
    print(f"10 + 5 = {result1}")
    print()
    
    # Test case 2: Subtraction
    print("Test 2: Subtraction")
    result2 = calc.subtract(10, 5)
    print(f"10 - 5 = {result2}")
    result2b = calc.subtract(5, 10)
    print(f"5 - 10 = {result2b}")
    print()
    
    # Test case 3: Multiplication
    print("Test 3: Multiplication")
    result3 = calc.multiply(10, 5)
    print(f"10 * 5 = {result3}")
    result3b = calc.multiply(-3, 4)
    print(f"-3 * 4 = {result3b}")
    print()
    
    # Test case 4: Division
    print("Test 4: Division")
    result4 = calc.divide(10, 5)
    print(f"10 / 5 = {result4}")
    result4b = calc.divide(7, 2)
    print(f"7 / 2 = {result4b}")
    print()
    
    # Test case 5: Division by zero (error handling)
    print("Test 5: Division by zero")
    try:
        result5 = calc.divide(10, 0)
        print(f"10 / 0 = {result5}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    print()
    
    # Test case 6: Floating point operations
    print("Test 6: Floating point operations")
    result6a = calc.add(3.5, 2.7)
    print(f"3.5 + 2.7 = {result6a}")
    result6b = calc.multiply(2.5, 4)
    print(f"2.5 * 4 = {result6b}")
    result6c = calc.divide(15.5, 2.5)
    print(f"15.5 / 2.5 = {result6c}")
    print()
    
    # Test case 7: Negative numbers
    print("Test 7: Negative numbers")
    result7a = calc.add(-5, 3)
    print(f"-5 + 3 = {result7a}")
    result7b = calc.subtract(-5, -3)
    print(f"-5 - (-3) = {result7b}")
    result7c = calc.multiply(-2, -3)
    print(f"-2 * -3 = {result7c}")
