# ALPHABET A PARTIR DE
import sys

letter = sys.argv[1]
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
start = alphabet.index(letter.lower())
print(alphabet[start:])