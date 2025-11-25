import re

text = "The quick brown fox jumps over the lazy dog."
pattern = r"fox"  # Raw string for regex pattern

match = re.search(pattern, text)

if match:
    print(f"Match found: {match.group()}")
    print(f"Start index: {match.start()}")
    print(f"End index: {match.end()}")
    print(text[match.start():match.end()])
else:
    print("No match found.")