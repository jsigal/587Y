# 2. One or more of a certain character and output
import re

text = "aaabbcdefg"
pattern = r"a+" # Matches one or more 'a' characters

match = re.search(pattern, text)
if match:
    print(f"Match for 'a+': {match.group()}")