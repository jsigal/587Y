# 3. Match at the Beginning or End of a String
import re

text1 = "Start of the string"
text2 = "End of the string"

if re.search(r"^Start", text1):
    print("Text1 starts with 'Start'")
if re.search(r"string$", text2):
    print("Text2 ends with 'string'")