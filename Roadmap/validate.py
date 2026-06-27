
import re
email = input("What's your email? ").strip()


pattern = r"^[a-zA-Z0-9_\.]+@(\w+\.)?[a-zA-Z0-9_]+\.[a-z]+$"

if re.search(pattern, email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


# ^ matches the start of the string
# $ matches the end of the string

# [] set of characters
# [^] not
# {n} n times of the character

# re.ignorecase --> ignores lower case or uppercase


