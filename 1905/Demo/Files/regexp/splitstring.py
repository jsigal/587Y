import re

text = "apple,banana;orange grapes"
pattern = r"[,; ]+"  # Matches one or more commas, semicolons, or spaces

parts = re.split(pattern, text)

print(f"Split parts: {parts}")