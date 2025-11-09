# 3. Find Maximum in a List
# Problem: Use a function to find the maximum value of all numbers in a list.

def find_max(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

data = [5, 12, 3, 8, 15]
print(f"The maximum in {data} is {find_max(data)}")

