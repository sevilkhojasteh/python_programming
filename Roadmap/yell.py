def main():
    # yell("This is CS50")
    yell(["This", "is", "CS50"])

# def yell(*words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()