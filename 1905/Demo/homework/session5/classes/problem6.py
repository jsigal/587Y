# 6.	Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting and deleting nodes.

class Node:
    """Represents a node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Represents a linked list data structure."""
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
    
    def display(self):
        """Display all elements in the linked list."""
        if self.head is None:
            print("Linked list is empty")
            return
        
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))
    
    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        """Insert a node at the end of the linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    
    def insert_at_position(self, data, position):
        """Insert a node at a specific position (0-indexed)."""
        if position < 0:
            print("Position must be non-negative")
            return
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        current = self.head
        for i in range(position - 1):
            if current is None:
                print(f"Position {position} is out of range")
                return
            current = current.next
        
        if current is None:
            print(f"Position {position} is out of range")
            return
        
        new_node.next = current.next
        current.next = new_node
    
    def delete_by_value(self, value):
        """Delete the first node with the given value."""
        if self.head is None:
            print("Linked list is empty")
            return False
        
        if self.head.data == value:
            self.head = self.head.next
            return True
        
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return True
            current = current.next
        
        print(f"Value {value} not found in the linked list")
        return False
    
    def delete_by_position(self, position):
        """Delete a node at a specific position (0-indexed)."""
        if self.head is None:
            print("Linked list is empty")
            return False
        
        if position < 0:
            print("Position must be non-negative")
            return False
        
        if position == 0:
            self.head = self.head.next
            return True
        
        current = self.head
        for i in range(position - 1):
            if current is None or current.next is None:
                print(f"Position {position} is out of range")
                return False
            current = current.next
        
        if current.next is None:
            print(f"Position {position} is out of range")
            return False
        
        current.next = current.next.next
        return True
    
    def size(self):
        """Return the number of nodes in the linked list."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count


# Test the implementation
if __name__ == "__main__":
    print("=" * 50)
    print("Linked List Implementation Test")
    print("=" * 50)
    
    # Create a new linked list
    ll = LinkedList()
    
    # Test 1: Display empty list
    print("\n1. Display empty linked list:")
    ll.display()
    
    # Test 2: Insert at beginning
    print("\n2. Inserting nodes at the beginning:")
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(30)
    ll.display()
    
    # Test 3: Insert at end
    print("\n3. Inserting nodes at the end:")
    ll.insert_at_end(40)
    ll.insert_at_end(50)
    ll.display()
    
    # Test 4: Insert at specific position
    print("\n4. Inserting node at position 2:")
    ll.insert_at_position(25, 2)
    ll.display()
    
    # Test 5: Get size
    print(f"\n5. Size of linked list: {ll.size()}")
    
    # Test 6: Delete by value
    print("\n6. Deleting node with value 25:")
    ll.delete_by_value(25)
    ll.display()
    
    # Test 7: Delete by position
    print("\n7. Deleting node at position 0:")
    ll.delete_by_position(0)
    ll.display()
    
    # Test 8: Delete non-existent value
    print("\n8. Attempting to delete non-existent value (99):")
    ll.delete_by_value(99)
    ll.display()
    
    # Test 9: Delete at invalid position
    print("\n9. Attempting to delete at invalid position (10):")
    ll.delete_by_position(10)
    ll.display()
    
    # Test 10: Final state
    print("\n10. Final linked list state:")
    ll.display()
    print(f"Final size: {ll.size()}")
    
    print("\n" + "=" * 50)
    print("All tests completed!")
    print("=" * 50)