# first, last = input("What's your name? ").split(" ")

# print(f"First name: {first}")

def total(galleons, sickles, knuts):
    return galleons * 493 + sickles * 29 + knuts

# coins = [100, 50, 25]
# print(total(*coins), "Knuts")

coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins), "knuts")

# *args, **kwargs