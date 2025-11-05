"""
Exercise 2.1 Arithmetic and Numeric Types
Ex2_1.py
"""

print('This is exercise 2.1')

# Part A
num1 = '5'
num2 = '9'

# explicit
num1 = int(num1) # convert num1 to an integer
num2 = int(num2) # convert numb2 to an integer
result = num1/num2 # do the division
print("The restult is", result) # display the result of the division
# pythonic
print(int(num1) / int(num2))

# Part B
paris_temp = '25'
honolulu_temp = '81'
freezing = 32.0
paris_temp = int(paris_temp)
honolulu_temp = int(honolulu_temp)
paris_temp_far = (paris_temp * (9/5)) + freezing
honolulu_temp_cel = (honolulu_temp-freezing) * (5/9)
print('paris in is ', paris_temp, "C  or ", paris_temp_far, "F")
print('honolulu in is ', honolulu_temp_cel, "C  or ", honolulu_temp, "F")
  

# Part C
price = '199.95'
price = float(price)

discount_small = .05
discount_med = .10
discount_big = .15

print("the original price is ", price, 'small discount is ', price - (price * discount_small))
print("the original price is ", price, 'med discount is ', price - (price * discount_med))
print("the original price is ", price, 'big discount is ', price - (price * discount_big))

