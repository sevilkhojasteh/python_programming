def main():
    name = input("What's your name? ")
    hello(name)
    goodbye(name)


def hello(name):
    print(f"Hello, {name}")


def goodbye(name):
    print(f"Goodbye, {name}")


if __name__ == "__main__":
    main()
