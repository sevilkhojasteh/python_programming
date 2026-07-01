# def meow(n: int) -> None:
#     for _ in range(n):
#         print("meow")


# number: int = int(input("How many times do you want to meow? "))
# meows: str = meow(number)
# print(meows)

# meow(number)

# def meow(n: int) ->str:
#     """
#     Meow n times.

#     :param n: Number of times to meow
#     :type n: int
#     :raise TypeError: If n is not an int
#     :return: A string of n meows, one per line
#     :rtype: str
#     """
#     return "meow\n" * n

# number: int = int(input("How many times do you want to meow? "))
# meows: str = meow(number)
# print(meows)

# meow(number)


# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("Usage: meows.py")
#     sys.exit(1)


import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")