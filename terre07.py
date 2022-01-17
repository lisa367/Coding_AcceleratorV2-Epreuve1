# TAILLE D'UNE CHAINE

import sys

try:
    if len(sys.argv) == 2:
        print(len(sys.argv[1]))
    else:
        print("Ce programme n'accepte qu'un seul argument.\nVeuillez réessayer.")
except TypeError:
    print('Erreur. Ce programme ne peut prendre qu\'une chaîne de caractères comme argument.')
