# RACINE CARREE D'UN NOMBRE

from math import sqrt
import sys

try:
    if int(sys.argv[1]) > 0:
        print( int(sqrt( int(sys.argv[1])) ) )
    else:
        print("L'argument ne peut pas être négatif.\nVeuillez réessayer.")
except ValueError:
    print("Ce programme n'accepte que des nombres entiers positifs en argument.\nVeuillez réessayer.")

