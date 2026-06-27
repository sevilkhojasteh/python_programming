def main():
    name = input("What's your name? ")
    print(hello(name))
    print(goodbye(name))


def hello(name):
    return f"Hello, {name}"


def goodbye(name):
    return f"Goodbye, {name}"


if __name__ == "__main__":
    main()