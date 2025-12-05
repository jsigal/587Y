# 9.	Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

class Queue:
    """
    A class representing a queue data structure (FIFO - First In First Out).
    """
    
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []
    
    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        
        Args:
            item: The item to be added to the queue.
        """
        self.items.append(item)
    
    def dequeue(self):
        """
        Remove and return the item from the front of the queue.
        
        Returns:
            The item removed from the front of the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self.items.pop(0)
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Return the number of items in the queue.
        
        Returns:
            The size of the queue.
        """
        return len(self.items)
    
    def peek(self):
        """
        Return the item at the front of the queue without removing it.
        
        Returns:
            The item at the front of the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue")
        return self.items[0]
    
    def __str__(self):
        """
        Return a string representation of the queue.
        
        Returns:
            A string representation of the queue.
        """
        return f"Queue({self.items})"


# Test the implementation
if __name__ == "__main__":
    print("=" * 50)
    print("Testing Queue Implementation")
    print("=" * 50)
    
    # Create a new queue
    queue = Queue()
    print(f"\n1. Created an empty queue: {queue}")
    print(f"   Is empty? {queue.is_empty()}")
    print(f"   Size: {queue.size()}")
    
    # Test enqueueing elements
    print("\n2. Enqueueing elements:")
    elements = [10, 20, 30, 40, 50]
    for element in elements:
        queue.enqueue(element)
        print(f"   Enqueued {element}: {queue}")
    
    print(f"\n   Queue after enqueueing: {queue}")
    print(f"   Is empty? {queue.is_empty()}")
    print(f"   Size: {queue.size()}")
    print(f"   Front element (peek): {queue.peek()}")
    
    # Test dequeueing elements
    print("\n3. Dequeueing elements:")
    while not queue.is_empty():
        dequeued = queue.dequeue()
        print(f"   Dequeued {dequeued}: {queue}")
    
    print(f"\n   Queue after dequeueing all: {queue}")
    print(f"   Is empty? {queue.is_empty()}")
    print(f"   Size: {queue.size()}")
    
    # Test with different data types
    print("\n4. Testing with different data types:")
    queue2 = Queue()
    queue2.enqueue("first")
    queue2.enqueue(42)
    queue2.enqueue([1, 2, 3])
    queue2.enqueue({"key": "value"})
    print(f"   Queue with mixed types: {queue2}")
    
    print("\n5. Dequeueing mixed types:")
    while not queue2.is_empty():
        item = queue2.dequeue()
        print(f"   Dequeued: {item} (type: {type(item).__name__})")
    
    # Test error handling
    print("\n6. Testing error handling:")
    empty_queue = Queue()
    try:
        empty_queue.dequeue()
    except IndexError as e:
        print(f"   ✓ Correctly raised IndexError: {e}")
    
    try:
        empty_queue.peek()
    except IndexError as e:
        print(f"   ✓ Correctly raised IndexError: {e}")
    
    print("\n" + "=" * 50)
    print("All tests completed!")
    print("=" * 50)