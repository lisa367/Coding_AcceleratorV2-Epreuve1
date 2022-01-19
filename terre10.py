# NOMBRE PREMIER

from math import sqrt
import sys
import math

try:
    n = int(sys.argv[1])
    if n == 0 or n == 1:
        print(f"Non, {n} n'est pas un nombre premier.")
        sys.exit()
    else:
        premier = False
        for x in list( range(2, math.floor(sqrt(n))+1) ):
            if n%x == 0:
                premier = True
                print(f"Non, {n} n'est pas un nombre premier.")
                break
            else:
                continue
        if premier == False:
            print(f"Oui, {n} est un nombre premier.")
except ValueError:
    print('Ce programme n\'accepte que des chiffres en arguments.\nVeuillez réessayer.\n')
