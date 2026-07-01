# def meow(n: int) -> None:
#     for _ in range(n):
#         print("meow")


# number: int = int(input("How many times do you want to meow? "))
# meows: str = meow(number)
# print(meows)

# meow(number)

def meow(n: int) ->str:
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n

number: int = int(input("How many times do you want to meow? "))
meows: str = meow(number)
print(meows)

# meow(number)