# PUISSANCE D'UN NOMBRE

import sys

try:
    if int(sys.argv[2]) > 0:
        print( int(sys.argv[1]) ** int(sys.argv[2]) )
    else:
        print("Le deuxième argument ne peut pas être négatif.\nVeuillez réessayer.")
except TypeError:
    print("Ce programme n'accepte que des entiers en argument.\nVeuillez réessayer.")
