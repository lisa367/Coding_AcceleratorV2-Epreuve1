# PAIR OU IMPAIR

import sys

try:
    input = int(sys.argv[1])
    # print(type(input))
except ValueError:
    print('Tu ne me la feras pas à l\'envers. Entre un nombre entier.')

if input < 0:
    input = input * (-1)
if input%2 == 0:
    print('pair')
else:
    print('impair')

