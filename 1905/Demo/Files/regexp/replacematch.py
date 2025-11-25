import re

text = "I have a red car and a blue car."
pattern = r"car"
replacement = "vehicle"

new_text = re.sub(pattern, replacement, text)

print(f"Original text: {text}")
print(f"Modified text: {new_text}")