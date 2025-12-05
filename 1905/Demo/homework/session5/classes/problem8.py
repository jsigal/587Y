# 8.	Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping and displaying elements.

class Stack:
    """
    A class representing a stack data structure (LIFO - Last In First Out).
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def push(self, item):
        """
        Add an element to the top of the stack.
        
        Args:
            item: The element to be added to the stack.
        """
        self.items.append(item)
        print(f"Pushed {item} to the stack")
    
    def pop(self):
        """
        Remove and return the top element from the stack.
        
        Returns:
            The top element of the stack, or None if the stack is empty.
        """
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_item = self.items.pop()
        print(f"Popped {popped_item} from the stack")
        return popped_item
    
    def display(self):
        """
        Display all elements in the stack from top to bottom.
        """
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements (top to bottom):")
            # Display from top (last element) to bottom (first element)
            for i in range(len(self.items) - 1, -1, -1):
                print(f"  {self.items[i]}")
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Return the number of elements in the stack.
        
        Returns:
            The size of the stack.
        """
        return len(self.items)


# Test the implementation
if __name__ == "__main__":
    print("=" * 50)
    print("Stack Data Structure Test")
    print("=" * 50)
    
    # Create a new stack
    stack = Stack()
    
    # Test 1: Display empty stack
    print("\n1. Display empty stack:")
    stack.display()
    
    # Test 2: Push elements
    print("\n2. Pushing elements to the stack:")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    
    # Test 3: Display stack after pushing
    print("\n3. Display stack after pushing elements:")
    stack.display()
    
    # Test 4: Pop elements
    print("\n4. Popping elements from the stack:")
    stack.pop()
    stack.pop()
    
    # Test 5: Display stack after popping
    print("\n5. Display stack after popping elements:")
    stack.display()
    
    # Test 6: Push more elements
    print("\n6. Pushing more elements:")
    stack.push(60)
    stack.push(70)
    
    # Test 7: Display final stack
    print("\n7. Final stack state:")
    stack.display()
    
    # Test 8: Pop all remaining elements
    print("\n8. Popping all remaining elements:")
    while not stack.is_empty():
        stack.pop()
    
    # Test 9: Try to pop from empty stack
    print("\n9. Attempting to pop from empty stack:")
    stack.pop()
    
    # Test 10: Display empty stack again
    print("\n10. Display empty stack:")
    stack.display()
    
    print("\n" + "=" * 50)
    print("All tests completed!")
    print("=" * 50)