# INVERSER UNE CHAINE

import sys

'''
print(sys.argv, end='\n')
print(len(sys.argv))
print(type(sys.argv))
'''

def reverse(string):
    new_string = ''
    for i in range(1, len(str(string))+1 ):
        new_string += string[-i]
    return new_string

for x in range(1, (len(sys.argv)) ):
    #print(reverse(sys.argv[-x]))
    print(reverse(sys.argv[-x]))
