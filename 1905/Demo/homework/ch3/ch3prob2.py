# 2. Even or Odd Counter
# Problem: Count how many numbers in a given list are even and how many are odd. 

numbers = [1, 4, 7, 10, 15, 20, 22, 25]
even_count = 0
odd_count = 0

for num in numbers:
    # Use the modulo operator to check if a number is even (remainder is 0)
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)
