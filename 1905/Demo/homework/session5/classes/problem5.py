# 5.	Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

class Stack:
    """A class representing a stack data structure (LIFO - Last In First Out)."""
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def push(self, element):
        """Add an element to the top of the stack.
        
        Args:
            element: The element to be added to the stack.
        """
        self.items.append(element)
    
    def pop(self):
        """Remove and return the top element from the stack.
        
        Returns:
            The top element of the stack.
            
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return the top element without removing it.
        
        Returns:
            The top element of the stack.
            
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0
    
    def size(self):
        """Return the number of elements in the stack.
        
        Returns:
            The size of the stack.
        """
        return len(self.items)
    
    def __str__(self):
        """Return a string representation of the stack."""
        return f"Stack({self.items})"


# Test the implementation
if __name__ == "__main__":
    # Create a new stack
    stack = Stack()
    print("Created an empty stack")
    print(f"Stack is empty: {stack.is_empty()}")
    print(f"Stack size: {stack.size()}")
    print()
    
    # Push elements onto the stack
    print("Pushing elements onto the stack:")
    stack.push(10)
    print(f"Pushed 10: {stack}")
    stack.push(20)
    print(f"Pushed 20: {stack}")
    stack.push(30)
    print(f"Pushed 30: {stack}")
    stack.push(40)
    print(f"Pushed 40: {stack}")
    print()
    
    # Check stack status
    print(f"Stack is empty: {stack.is_empty()}")
    print(f"Stack size: {stack.size()}")
    print(f"Top element (peek): {stack.peek()}")
    print()
    
    # Pop elements from the stack
    print("Popping elements from the stack:")
    print(f"Popped: {stack.pop()}")
    print(f"Stack after pop: {stack}")
    print(f"Popped: {stack.pop()}")
    print(f"Stack after pop: {stack}")
    print(f"Popped: {stack.pop()}")
    print(f"Stack after pop: {stack}")
    print()
    
    # Check stack status again
    print(f"Stack is empty: {stack.is_empty()}")
    print(f"Stack size: {stack.size()}")
    print()
    
    # Pop remaining element
    print(f"Popped: {stack.pop()}")
    print(f"Stack after pop: {stack}")
    print()
    
    # Try to pop from empty stack (should raise an error)
    print("Attempting to pop from empty stack:")
    try:
        stack.pop()
    except IndexError as e:
        print(f"Error caught: {e}")
    print()
    
    # Test with different data types
    print("Testing with different data types:")
    stack2 = Stack()
    stack2.push("first")
    stack2.push("second")
    stack2.push("third")
    print(f"String stack: {stack2}")
    print(f"Popped: {stack2.pop()}")
    print(f"Popped: {stack2.pop()}")
    print(f"Popped: {stack2.pop()}")
    print(f"Final stack: {stack2}")