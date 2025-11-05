"""
Exercise 2.1 Arithmetic and Numeric Types
Ex2_1_EndPoint.py
"""

print('This is exercise 2.1')

# Part A
num1 = '5'
num2 = '9'

print('Floating point division result is', float(num1) / float(num2))


# Part B
paris_temp = '25'
honolulu_temp = '81'
freezing = 32.0

paris_tempc = float(paris_temp)
honolulu_tempf = float(honolulu_temp)

paris_tempf = paris_tempc * 9.0 / 5.0 + freezing
honolulu_tempc = (honolulu_tempf - freezing) * 5.0 / 9.0

print('The Celsius temperature in Paris is', paris_tempc)
print('The Fahrenheit temperature in Paris is', paris_tempf)
print('The Celsius temperature in Honolulu is', honolulu_tempc)
print('The Fahrenheit temperature in Honolulu is', honolulu_tempf)

# Part C
price = 199.95

discount_small = .05
discount_med = .10
discount_big = .15

