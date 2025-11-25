import re

# The string to search within
text = "My phone number is 123-456-7890, and my friend's is 987.654.3210."

# The regular expression pattern to match one or more digits
# \d matches any digit (0-9)
# + matches one or more occurrences of the preceding character (in this case, \d)
pattern = r'\d+'

# Use re.findall() to find all non-overlapping matches of the pattern in the string
matches = re.findall(pattern, text)

# Print the found matches
print(f"Original text: {text}")
print(f"Found digits: {matches}")