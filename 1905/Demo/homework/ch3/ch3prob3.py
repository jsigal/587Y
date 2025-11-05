# 3. Price Look-up in a Dictionary
# Problem: Given a dictionary of items and their prices, find and print the price of a specific item if it exists. If it doesn't, print an error message. 

prices = {
    'apple': 0.50,
    'banana': 0.25,
    'orange': 0.75,
    'grape': 1.25
}

item_to_find = 'banana'
# item_to_find = 'kiwi' # Use this to test the 'else' condition

# Check if the item exists in the dictionary
if item_to_find in prices:
    price = prices[item_to_find]
    print("The price of", item_to_find, "is $", price)
else:
    print("Sorry, that item is not found.")

