# 7. Character Frequency Counter
# Count the frequency of each character in a given string and store the counts in a 

text = "hello world"
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1
print(f"Character frequencies: {frequency}")
