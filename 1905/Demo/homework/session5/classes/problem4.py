# 4.	Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.

class Node:
    """Represents a node in the binary search tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.value)


class BinarySearchTree:
    """Represents a binary search tree with insert and search functionality."""
    
    def __init__(self):
        """Initialize an empty binary search tree."""
        self.root = None
    
    def insert(self, value):
        """
        Insert a value into the binary search tree.
        
        Args:
            value: The value to insert into the tree.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """
        Helper method to recursively insert a value into the tree.
        
        Args:
            node: Current node in the tree.
            value: Value to insert.
        """
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
        # If value == node.value, we don't insert duplicates (or you could handle it differently)
    
    def search(self, value):
        """
        Search for a value in the binary search tree.
        
        Args:
            value: The value to search for.
            
        Returns:
            True if the value is found, False otherwise.
        """
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """
        Helper method to recursively search for a value in the tree.
        
        Args:
            node: Current node in the tree.
            value: Value to search for.
            
        Returns:
            True if the value is found, False otherwise.
        """
        if node is None:
            return False
        
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def inorder_traversal(self):
        """
        Perform an inorder traversal of the tree (for display purposes).
        
        Returns:
            List of values in sorted order.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)


# Test the implementation
if __name__ == "__main__":
    # Create a new binary search tree
    bst = BinarySearchTree()
    
    # Test 1: Insert elements
    print("Test 1: Inserting elements into the BST")
    values_to_insert = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    print(f"Inserting values: {values_to_insert}")
    for value in values_to_insert:
        bst.insert(value)
    
    # Display the tree using inorder traversal (should show sorted order)
    print(f"Inorder traversal (sorted): {bst.inorder_traversal()}")
    print()
    
    # Test 2: Search for existing elements
    print("Test 2: Searching for existing elements")
    search_values = [50, 30, 70, 10, 80, 35]
    for value in search_values:
        result = bst.search(value)
        print(f"Search for {value}: {'Found' if result else 'Not Found'}")
    print()
    
    # Test 3: Search for non-existing elements
    print("Test 3: Searching for non-existing elements")
    non_existing = [5, 55, 100, 15]
    for value in non_existing:
        result = bst.search(value)
        print(f"Search for {value}: {'Found' if result else 'Not Found'}")
    print()
    
    # Test 4: Insert and search in empty tree
    print("Test 4: Creating a new empty tree")
    empty_bst = BinarySearchTree()
    print(f"Search in empty tree for 10: {'Found' if empty_bst.search(10) else 'Not Found'}")
    empty_bst.insert(42)
    print(f"After inserting 42, search for 42: {'Found' if empty_bst.search(42) else 'Not Found'}")
    print()
    
    # Test 5: Single element tree
    print("Test 5: Single element tree")
    single_bst = BinarySearchTree()
    single_bst.insert(100)
    print(f"Search for 100: {'Found' if single_bst.search(100) else 'Not Found'}")
    print(f"Search for 50: {'Found' if single_bst.search(50) else 'Not Found'}")
    print()
    
    # Test 6: All test results summary
    print("=" * 50)
    print("All tests completed successfully!")
    print("=" * 50)