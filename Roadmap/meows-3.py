# def meow(n: int) -> None:
#     for _ in range(n):
#         print("meow")


# number: int = int(input("How many times do you want to meow? "))
# meows: str = meow(number)
# print(meows)

# meow(number)

def meow(n: int) ->str:
    return "meow\n" * n

number: int = int(input("How many times do you want to meow? "))
meows: str = meow(number)
print(meows)

# meow(number)