from enum import Enum

class ProductType(Enum):
    ELECTRONICS = "electronics"
    CLOTHING = "clothing"
    BOOKS = "books"

class Product:
    def __init__(self, name, product_type):
        self.name = name
        self.product_type = product_type

laptop = Product("Laptop", ProductType.ELECTRONICS)
shirt = Product("T-shirt", ProductType.CLOTHING)

print(f"{laptop.name} is a {laptop.product_type.value} product.")