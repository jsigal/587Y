# 2. Sum of List Elements
# Problem: Use a function to calculate the sum of all numbers in a list.

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_list = [10, 20, 30, 40]
print(f"The sum of {my_list} is {sum_list(my_list)}")