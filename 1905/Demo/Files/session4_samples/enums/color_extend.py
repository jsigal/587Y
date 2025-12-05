from enum import Enum

class Color(Enum):
    RED = (1, "#FF0000", "Ruby Red")
    GREEN = (2, "#00FF00", "Guava Green")
    BLUE = (3, "#0000FF", "Baby Blue")

    def __init__(self, value, hex_code, description):
        self._value_ = value  # Assign the primary value
        self.hex_code = hex_code
        self.description = description

# Accessing the enum members and their attributes
print(f"Color: {Color.RED.name}")
print(f"Value: {Color.RED.value}")
print(f"Hex Code: {Color.RED.hex_code}")
print(f"Description: {Color.RED.description}")

print(f"\nColor: {Color.GREEN.name}")
print(f"Value: {Color.GREEN.value}")
print(f"Hex Code: {Color.GREEN.hex_code}")
print(f"Description: {Color.GREEN.description}")