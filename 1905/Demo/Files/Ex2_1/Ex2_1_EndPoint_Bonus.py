"""
Exercise 2.1 Arithmetic and Numeric Types
Ex2_1_EndPoint_Bonus.py
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
print('The Fahrehneit temperature in Honolulu is', honolulu_tempf)

# Part C
price = 199.95

discount_small = .05
discount_med = .10
discount_big = .15

price_small = price - (price * discount_small)
price_med = price - (price * discount_med)
price_big = price - (price * discount_big)

print('The original price is', price)
print('The price with discount_small', discount_small, 'is', price_small)
print('The price with discount_med', discount_med, 'is', price_med)
print('The price with discount_big', discount_big, 'is', price_big)

dist1 = 305.0
dist2 = 525.0
time1 = 62.0
time2 = 91.0
mtok = 1.6

print('the speed for flight 1 in miles per hour is', (dist1 / time1 * 60))
print('the speed for flight 1 in kilometers per hour is', (dist1 / time1 * 60 * mtok))
print('the speed for flight 2 in miles per hour is', (dist2 / time2 * 60))
print('the speed for flight 2 in kilometers per hour is', (dist2 / time2 * 60 * mtok))

avg = (dist1 + dist2) / (time1 + time2) * 60
print('the average speed for both flights in miles per hour is', avg)

avg = (dist1 + dist2) / (time1 + time2) * 60 * mtok
print('the average speed for both flights in kilometers per hour is', avg)


import math
area = 7.5

rad = math.sqrt(area / math.pi)
print('cirle with area of', area, 'has radius of', rad)
