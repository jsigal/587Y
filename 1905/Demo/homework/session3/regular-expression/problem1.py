# 1. Pattern match a phone number and output it
import re

text = "My phone number is 123-456-7890."
pattern = r"\d{3}-\d{3}-\d{4}" # Matches a phone number pattern

match = re.search(pattern, text)
if match:
    print(f"Phone number found: {match.group()}")