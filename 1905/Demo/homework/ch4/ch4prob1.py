# 1. Fibonacci Sequence Generator
#Problem: Generate the first n terms of the Fibonacci sequence using a generator. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.

def fibonacci_generator(n_terms):
    a, b = 0, 1
    count = 0
    while count < n_terms:
        yield a
        # Update variables using arithmetic operators
        temp = a
        a = b
        b = temp + b
        count += 1

# Using the generator
terms = 10
fib_sequence = []
for number in fibonacci_generator(terms):
    fib_sequence.append(number)
print(f"Fibonacci sequence of {terms} terms: {fib_sequence}")
