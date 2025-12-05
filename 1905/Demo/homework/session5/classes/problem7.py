# 7.	Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    """
    A class representing a shopping cart that can hold items with prices.
    """
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = {}  # Dictionary to store items: {item_name: {'price': price, 'quantity': quantity}}
    
    def add_item(self, item_name, price, quantity=1):
        """
        Add an item to the shopping cart.
        
        Args:
            item_name (str): Name of the item
            price (float): Price per unit of the item
            quantity (int): Quantity to add (default is 1)
        
        Returns:
            None
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if price < 0:
            raise ValueError("Price cannot be negative")
        
        if item_name in self.items:
            # If item already exists, update the quantity
            self.items[item_name]['quantity'] += quantity
        else:
            # Add new item
            self.items[item_name] = {'price': price, 'quantity': quantity}
    
    def remove_item(self, item_name, quantity=None):
        """
        Remove an item from the shopping cart.
        
        Args:
            item_name (str): Name of the item to remove
            quantity (int, optional): Quantity to remove. If None, removes all of that item.
        
        Returns:
            bool: True if item was removed, False if item not found
        """
        if item_name not in self.items:
            return False
        
        if quantity is None:
            # Remove all of this item
            del self.items[item_name]
            return True
        else:
            # Remove specified quantity
            if quantity <= 0:
                raise ValueError("Quantity must be greater than 0")
            
            self.items[item_name]['quantity'] -= quantity
            
            # If quantity becomes 0 or negative, remove the item completely
            if self.items[item_name]['quantity'] <= 0:
                del self.items[item_name]
            
            return True
    
    def calculate_total(self):
        """
        Calculate the total price of all items in the cart.
        
        Returns:
            float: Total price of all items
        """
        total = 0.0
        for item_name, item_data in self.items.items():
            total += item_data['price'] * item_data['quantity']
        return total
    
    def get_item_count(self):
        """
        Get the total number of items (by quantity) in the cart.
        
        Returns:
            int: Total quantity of all items
        """
        return sum(item_data['quantity'] for item_data in self.items.values())
    
    def get_unique_item_count(self):
        """
        Get the number of unique items in the cart.
        
        Returns:
            int: Number of unique items
        """
        return len(self.items)
    
    def display_cart(self):
        """
        Display the contents of the shopping cart.
        
        Returns:
            str: Formatted string representation of the cart
        """
        if not self.items:
            return "Shopping cart is empty."
        
        cart_str = "Shopping Cart:\n"
        cart_str += "-" * 50 + "\n"
        for item_name, item_data in self.items.items():
            cart_str += f"{item_name:20} ${item_data['price']:8.2f} x {item_data['quantity']:3} = ${item_data['price'] * item_data['quantity']:8.2f}\n"
        cart_str += "-" * 50 + "\n"
        cart_str += f"{'Total:':20} ${self.calculate_total():8.2f}\n"
        return cart_str
    
    def clear(self):
        """Clear all items from the shopping cart."""
        self.items.clear()
    
    def __str__(self):
        """String representation of the shopping cart."""
        return self.display_cart()
    
    def __repr__(self):
        """Official string representation of the shopping cart."""
        return f"ShoppingCart(items={len(self.items)}, total=${self.calculate_total():.2f})"


# Test the implementation
if __name__ == "__main__":
    print("=" * 60)
    print("Testing ShoppingCart Implementation")
    print("=" * 60)
    
    # Create a new shopping cart
    cart = ShoppingCart()
    print("\n1. Created an empty shopping cart")
    print(f"   Cart: {cart}")
    print(f"   Unique items: {cart.get_unique_item_count()}")
    print(f"   Total items: {cart.get_item_count()}")
    print(f"   Total price: ${cart.calculate_total():.2f}")
    
    # Add items to the cart
    print("\n2. Adding items to the cart...")
    cart.add_item("Apple", 0.99, 5)
    cart.add_item("Banana", 0.59, 3)
    cart.add_item("Milk", 3.49, 2)
    cart.add_item("Bread", 2.99, 1)
    print(cart)
    
    # Add more of an existing item
    print("\n3. Adding more apples...")
    cart.add_item("Apple", 0.99, 3)
    print(cart)
    
    # Remove some items
    print("\n4. Removing 2 bananas...")
    cart.remove_item("Banana", 2)
    print(cart)
    
    # Remove an item completely
    print("\n5. Removing all bread...")
    cart.remove_item("Bread")
    print(cart)
    
    # Calculate total
    print("\n6. Calculating total price...")
    total = cart.calculate_total()
    print(f"   Total price: ${total:.2f}")
    
    # Test edge cases
    print("\n7. Testing edge cases...")
    
    # Try to remove non-existent item
    result = cart.remove_item("NonExistentItem")
    print(f"   Removing non-existent item: {result}")
    
    # Add item with custom quantity
    cart.add_item("Eggs", 4.99, 1)
    print(f"\n   After adding eggs:\n{cart}")
    
    # Clear the cart
    print("\n8. Clearing the cart...")
    cart.clear()
    print(f"   Cart after clearing: {cart}")
    print(f"   Total price: ${cart.calculate_total():.2f}")
    
    # Test with a new cart for comprehensive testing
    print("\n9. Comprehensive test with new cart...")
    cart2 = ShoppingCart()
    cart2.add_item("Laptop", 999.99, 1)
    cart2.add_item("Mouse", 29.99, 2)
    cart2.add_item("Keyboard", 79.99, 1)
    cart2.add_item("USB Cable", 9.99, 3)
    print(cart2)
    print(f"   Unique items: {cart2.get_unique_item_count()}")
    print(f"   Total items: {cart2.get_item_count()}")
    print(f"   Total price: ${cart2.calculate_total():.2f}")
    
    # Test error handling
    print("\n10. Testing error handling...")
    try:
        cart2.add_item("Test", -5.00)  # Negative price
    except ValueError as e:
        print(f"   Caught error (negative price): {e}")
    
    try:
        cart2.add_item("Test", 5.00, -1)  # Negative quantity
    except ValueError as e:
        print(f"   Caught error (negative quantity): {e}")
    
    try:
        cart2.remove_item("Test", -1)  # Negative quantity
    except ValueError as e:
        print(f"   Caught error (negative remove quantity): {e}")
    
    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)