import timeit

# Define the code snippets to be timed
code_snippet_1 = '"-".join(str(n) for n in range(100))'
code_snippet_2 = '", ".join([str(n) for n in range(100)])'
code_snippet_3 = '", ".join(map(str, range(100)))'

# Time the execution of each snippet
# The 'number' argument specifies how many times the code snippet will be executed.
# The 'setup' argument can be used to provide setup code that is executed once.
time_1 = timeit.timeit(stmt=code_snippet_1, number=10000)
time_2 = timeit.timeit(stmt=code_snippet_2, number=10000)
time_3 = timeit.timeit(stmt=code_snippet_3, number=10000)

print(f"Time for generator expression: {time_1:.6f} seconds")
print(f"Time for list comprehension: {time_2:.6f} seconds")
print(f"Time for map function: {time_3:.6f} seconds")

# You can also time functions directly
def using_generator():
    "-".join(str(n) for n in range(100))

def using_list_comprehension():
    ", ".join([str(n) for n in range(100)])

def using_map():
    ", ".join(map(str, range(100)))

time_func_1 = timeit.timeit(using_generator, number=10000)
time_func_2 = timeit.timeit(using_list_comprehension, number=10000)
time_func_3 = timeit.timeit(using_map, number=10000)

print(f"\nTime for function using generator expression: {time_func_1:.6f} seconds")
print(f"Time for function using list comprehension: {time_func_2:.6f} seconds")
print(f"Time for function using map function: {time_func_3:.6f} seconds")