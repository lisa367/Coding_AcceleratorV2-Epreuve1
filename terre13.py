# TROUVER LA SUISSE

import sys

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    z = int(sys.argv[3])
    input = [x, y, z]
except ValueError:
    print("Ce programme n'accepte que trois chiffres entiers comme arguments.\nVeuillez réessayer.")

try:
    if x == y or x == z or y == z:
        print("Erreur")
    else:
        input.sort()
        print(input[1])
except NameError:
    print('')

