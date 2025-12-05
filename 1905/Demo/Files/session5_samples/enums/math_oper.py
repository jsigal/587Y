from enum import Enum

# A helper class can be useful to wrap the lambda, especially for type hinting
# and to make it a descriptor that Enum won't ignore.
# The standard library approach often uses a method within the Enum itself
# or stores the function as a separate attribute.
# The simplest approach is to use a value wrapper as seen in search results.

class FunctionProxy:
    """Helper to store a callable function within an Enum value."""
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

class MathOperation(Enum):
    """
    An Enum where each member's value is a FunctionProxy wrapping a lambda.
    """
    ADD = FunctionProxy(lambda x, y: x + y)
    SUBTRACT = FunctionProxy(lambda x, y: x - y)
    MULTIPLY = FunctionProxy(lambda x, y: x * y)
    DIVIDE = FunctionProxy(lambda x, y: x / y)

    # You can also add methods directly to the Enum class
    def calculate(self, x, y):
        """A method to call the stored function for any given member."""
        return self.value(x, y)

# --- Usage Examples ---

# 1. Access the function directly through the .value attribute
result_add = MathOperation.ADD.value(10, 5)
print(f"Add (direct value call): 10 + 5 = {result_add}")

# 2. Use a shared method within the Enum class for a cleaner API
result_sub = MathOperation.SUBTRACT.calculate(10, 5)
print(f"Subtract (via calculate method): 10 - 5 = {result_sub}")

# 3. Iterate through operations
x_val = 20
y_val = 4
for op in MathOperation:
    # Use the calculate method for a consistent interface
    result = op.calculate(x_val, y_val)
    print(f"{op.name} result for {x_val}, {y_val}: {result}")
