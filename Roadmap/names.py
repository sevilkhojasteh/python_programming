names = []

for _ in range(3):
    names.append(input("What's your name? "))

file = open("names.txt", "a")
file.write("\n".join(sorted(names)))
file.close()

for name in sorted(names):
    print(f"hello, {name}")