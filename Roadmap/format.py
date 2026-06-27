import re
name = input("What's your name? ")



if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")


# ^ matches the start of the string
# $ matches the end of the string"

# := this operator not only assignes a value but also checks the bool form 

