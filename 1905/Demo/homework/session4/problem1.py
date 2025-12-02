# Create a class Greeter with a method greet(name) that prints a greeting for the provided name.

class Greeter:
    def greet(self, name):
        print(f"Hello, {name}!")

g = Greeter()
g.greet("Thomas")
Greeter().greet("Mimi")

class GreeterStatic:
    @staticmethod
    def greet(name):
        print(f"Hello, {name}!")

GreeterStatic.greet("Thomas")

