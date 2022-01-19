# TRIE OU PAS

import sys

input = sys.argv[1:]

try:
    for x in input:
        x = int(x)
    
    if input == sorted(input) :
        print('Triée !') 
    else:
        print("Pas triée !") 

except ValueError:
    print('Ce programme n\'accepte que des chiffres en arguments.\nVeuillez réessayer.\n')

