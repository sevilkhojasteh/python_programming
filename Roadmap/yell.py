def main():
    # yell("This is CS50")
    yell(["This", "is", "CS50"])

def yell(phrase):
    uppercased = []
    for word in phrase:
        uppercased.append(word.upper())
    print(" ".join(uppercased))




if __name__ == "__main__":
    main()