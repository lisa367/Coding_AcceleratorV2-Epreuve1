# DIVISION

import sys
import math

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
try:
    print(math.floor(num1/num2))
    print(num1%num2)
except ZeroDivisionError:
    print("The second argument cannot be 0. Please choose another number.")
