hauteur = int(input())

for i in range(1, hauteur + 1):
    print(" " * (hauteur - i), "* " * i)

for i in range(1, hauteur + 1):
    print(" " * i, "* " * (hauteur - i))