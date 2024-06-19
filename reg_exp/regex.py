import re

# string = "VIT.AP University"
# pattern = r"\." 

string = "It is raining outside"
pattern = r"^It"

match = re.search(pattern, string)

print(match)
