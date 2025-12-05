# Problem 2: Order Status Management
# •	Create an Enum: 
# Define an Enum called OrderStatus with members PENDING, PROCESSING, SHIPPED, and DELIVERED.
# •	Create a Class: 
# Define a class Order.
# •	It should have instance attributes order_id (integer) and status (initialized to OrderStatus.PENDING).
# •	Implement a method update_status(new_status) that takes an OrderStatus member as an argument and updates the order's status. Include error handling to ensure new_status is a valid OrderStatus member.
# •	Implement a method display_order_details() that prints the order ID and its current status.

from enum import Enum


class OrderStatus(Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"


class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.status = OrderStatus.PENDING
    
    def update_status(self, new_status):
        """Updates the order's status with error handling"""
        if not isinstance(new_status, OrderStatus):
            raise ValueError(f"Invalid status: {new_status}. Must be an OrderStatus enum member.")
        self.status = new_status
    
    def display_order_details(self):
        """Prints the order ID and its current status"""
        print(f"Order ID: {self.order_id}, Status: {self.status.value}")


# Test code
if __name__ == "__main__":
    # Create a new order
    order1 = Order(1001)
    print("Initial order:")
    order1.display_order_details()
    
    # Update status through the workflow
    print("\nUpdating status to PROCESSING:")
    order1.update_status(OrderStatus.PROCESSING)
    order1.display_order_details()
    
    print("\nUpdating status to SHIPPED:")
    order1.update_status(OrderStatus.SHIPPED)
    order1.display_order_details()
    
    print("\nUpdating status to DELIVERED:")
    order1.update_status(OrderStatus.DELIVERED)
    order1.display_order_details()
    
    # Test error handling
    print("\nTesting error handling with invalid status:")
    try:
        order1.update_status("INVALID_STATUS")
    except ValueError as e:
        print(f"Error caught: {e}")
    
    # Create another order and test
    print("\n" + "="*50)
    order2 = Order(1002)
    print("New order created:")
    order2.display_order_details()
    
    print("\nUpdating directly to SHIPPED:")
    order2.update_status(OrderStatus.SHIPPED)
    order2.display_order_details()

