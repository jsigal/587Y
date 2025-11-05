# 4. Sum of Multiples of 3 and 5
# Problem: Calculate the sum of all numbers between 1 and 20 (inclusive) that are multiples of 3 or 5.

total_sum = 0
start_num = 1
end_num = 20

# Loop through numbers from 1 up to (but not including) 21
for number in range(start_num, end_num + 1):
    # Check if the number is divisible by 3 OR divisible by 5
    if (number % 3 == 0) or (number % 5 == 0):
        total_sum = total_sum + number

print("The sum of multiples of 3 or 5 up to 20 is:", total_sum)
