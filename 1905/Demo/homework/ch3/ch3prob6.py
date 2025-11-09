# 6. Filter Even Numbers
# Problem: Create a new list containing only the even numbers from an existing list using a list comprehension.

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in original_list if num % 2 == 0]
print(f"Even numbers: {even_numbers}")
