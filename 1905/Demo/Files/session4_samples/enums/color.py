from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

for c in Color:
    print(f'{c} {c.name}={c.value}')