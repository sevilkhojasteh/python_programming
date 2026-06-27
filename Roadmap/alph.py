alphabet = []

with open("alph.csv") as file:
    for line in file:
        alpha, number = line.rstrip().split(",")
        alphas = {}
        alphas[alpha] = number
        alphabet.append(alphas)



