# 3.	Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """A base class to represent a shape with methods to calculate area and perimeter."""
    
    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.
        
        Returns:
            float: The area of the shape
        """
        pass
    
    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.
        
        Returns:
            float: The perimeter of the shape
        """
        pass
    
    def __str__(self):
        """Return a string representation of the shape."""
        return f"{self.__class__.__name__} with area: {self.area():.2f} and perimeter: {self.perimeter():.2f}"


class Circle(Shape):
    """A class to represent a circle."""
    
    def __init__(self, radius):
        """
        Initialize a Circle object.
        
        Args:
            radius (float): The radius of the circle (must be positive)
        
        Raises:
            ValueError: If radius is negative or zero
        """
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    
    def area(self):
        """
        Calculate and return the area of the circle.
        
        Returns:
            float: The area of the circle (π * r²)
        """
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """
        Calculate and return the perimeter (circumference) of the circle.
        
        Returns:
            float: The perimeter of the circle (2 * π * r)
        """
        return 2 * math.pi * self.radius
    
    def __str__(self):
        """Return a string representation of the circle."""
        return f"Circle with radius: {self.radius:.2f}, area: {self.area():.2f}, perimeter: {self.perimeter():.2f}"


class Triangle(Shape):
    """A class to represent a triangle."""
    
    def __init__(self, side1, side2, side3):
        """
        Initialize a Triangle object.
        
        Args:
            side1 (float): The length of the first side (must be positive)
            side2 (float): The length of the second side (must be positive)
            side3 (float): The length of the third side (must be positive)
        
        Raises:
            ValueError: If any side is non-positive or if the sides don't form a valid triangle
        """
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("All sides must be positive")
        
        # Check triangle inequality: sum of any two sides must be greater than the third
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise ValueError("Invalid triangle: the sum of any two sides must be greater than the third side")
        
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        """
        Calculate and return the area of the triangle using Heron's formula.
        
        Returns:
            float: The area of the triangle
        """
        s = self.perimeter() / 2  # Semi-perimeter
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        """
        Calculate and return the perimeter of the triangle.
        
        Returns:
            float: The perimeter of the triangle (sum of all three sides)
        """
        return self.side1 + self.side2 + self.side3
    
    def __str__(self):
        """Return a string representation of the triangle."""
        return f"Triangle with sides: {self.side1:.2f}, {self.side2:.2f}, {self.side3:.2f}, area: {self.area():.2f}, perimeter: {self.perimeter():.2f}"


class Square(Shape):
    """A class to represent a square."""
    
    def __init__(self, side):
        """
        Initialize a Square object.
        
        Args:
            side (float): The length of one side of the square (must be positive)
        
        Raises:
            ValueError: If side is negative or zero
        """
        if side <= 0:
            raise ValueError("Side length must be positive")
        self.side = side
    
    def area(self):
        """
        Calculate and return the area of the square.
        
        Returns:
            float: The area of the square (side²)
        """
        return self.side ** 2
    
    def perimeter(self):
        """
        Calculate and return the perimeter of the square.
        
        Returns:
            float: The perimeter of the square (4 * side)
        """
        return 4 * self.side
    
    def __str__(self):
        """Return a string representation of the square."""
        return f"Square with side: {self.side:.2f}, area: {self.area():.2f}, perimeter: {self.perimeter():.2f}"


# Test the implementation
if __name__ == '__main__':
    print("=" * 60)
    print("Testing Shape Classes")
    print("=" * 60)
    print()
    
    # Test case 1: Circle
    print("Test 1: Circle")
    try:
        circle1 = Circle(5.0)
        print(f"Circle 1: {circle1}")
        print(f"  Area: {circle1.area():.4f} square units")
        print(f"  Perimeter: {circle1.perimeter():.4f} units")
        print()
        
        circle2 = Circle(10)
        print(f"Circle 2: {circle2}")
        print(f"  Area: {circle2.area():.4f} square units")
        print(f"  Perimeter: {circle2.perimeter():.4f} units")
        print()
    except ValueError as e:
        print(f"Error: {e}")
    print()
    
    # Test case 2: Square
    print("Test 2: Square")
    try:
        square1 = Square(4.0)
        print(f"Square 1: {square1}")
        print(f"  Area: {square1.area():.4f} square units")
        print(f"  Perimeter: {square1.perimeter():.4f} units")
        print()
        
        square2 = Square(7.5)
        print(f"Square 2: {square2}")
        print(f"  Area: {square2.area():.4f} square units")
        print(f"  Perimeter: {square2.perimeter():.4f} units")
        print()
    except ValueError as e:
        print(f"Error: {e}")
    print()
    
    # Test case 3: Triangle
    print("Test 3: Triangle")
    try:
        triangle1 = Triangle(3, 4, 5)
        print(f"Triangle 1: {triangle1}")
        print(f"  Area: {triangle1.area():.4f} square units")
        print(f"  Perimeter: {triangle1.perimeter():.4f} units")
        print()
        
        triangle2 = Triangle(5, 6, 7)
        print(f"Triangle 2: {triangle2}")
        print(f"  Area: {triangle2.area():.4f} square units")
        print(f"  Perimeter: {triangle2.perimeter():.4f} units")
        print()
        
        # Equilateral triangle
        triangle3 = Triangle(6, 6, 6)
        print(f"Triangle 3 (Equilateral): {triangle3}")
        print(f"  Area: {triangle3.area():.4f} square units")
        print(f"  Perimeter: {triangle3.perimeter():.4f} units")
        print()
    except ValueError as e:
        print(f"Error: {e}")
    print()
    
    # Test case 4: Error handling - invalid circle
    print("Test 4: Error handling - invalid circle")
    try:
        invalid_circle = Circle(-5)
        print(f"Invalid circle: {invalid_circle}")
    except ValueError as e:
        print(f"  Expected error caught: {e}")
    print()
    
    # Test case 5: Error handling - invalid square
    print("Test 5: Error handling - invalid square")
    try:
        invalid_square = Square(0)
        print(f"Invalid square: {invalid_square}")
    except ValueError as e:
        print(f"  Expected error caught: {e}")
    print()
    
    # Test case 6: Error handling - invalid triangle
    print("Test 6: Error handling - invalid triangle")
    try:
        invalid_triangle = Triangle(1, 2, 5)
        print(f"Invalid triangle: {invalid_triangle}")
    except ValueError as e:
        print(f"  Expected error caught: {e}")
    print()
    
    # Test case 7: Polymorphism - storing different shapes in a list
    print("Test 7: Polymorphism - different shapes in a list")
    shapes = [
        Circle(3),
        Square(5),
        Triangle(3, 4, 5),
        Circle(2),
        Square(6)
    ]
    
    print("Processing shapes using polymorphism:")
    for i, shape in enumerate(shapes, 1):
        print(f"  Shape {i}: {shape.__class__.__name__}")
        print(f"    Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")
    print()
    
    # Test case 8: Total area and perimeter of all shapes
    print("Test 8: Total area and perimeter of all shapes")
    total_area = sum(shape.area() for shape in shapes)
    total_perimeter = sum(shape.perimeter() for shape in shapes)
    print(f"  Total area of all shapes: {total_area:.2f} square units")
    print(f"  Total perimeter of all shapes: {total_perimeter:.2f} units")
    print()
    
    print("=" * 60)
    print("All tests completed!")
    print("=" * 60)
