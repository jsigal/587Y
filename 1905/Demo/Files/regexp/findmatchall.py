import re

text = "The year is 2025, and the next year is 2026."
pattern = r"\d{4}"  # Matches any four consecutive digits

all_matches = re.findall(pattern, text)

print(f"All 4-digit numbers: {all_matches}")