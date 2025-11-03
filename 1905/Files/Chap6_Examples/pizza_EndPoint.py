# Add import statements at the top of the source code

import itertools

toppings = ['pepperoni', 'cheese', 'ham', 'bacon',
            'mushrooms', 'peppers', 'onions', 'olives']

num_toppings = 3

# Create a for loop to process the iterator

for tops in itertools.combinations(toppings, num_toppings):
    print('Pizza with', tops)
