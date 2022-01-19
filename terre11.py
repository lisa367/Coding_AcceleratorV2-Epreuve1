# 24 TO 12

import sys
import datetime as dt

input = sys.argv[1]
format24h = dt.datetime.strptime(input, '%H:%M')
format12h = dt.datetime.strftime(format24h, '%I:%M%p')

print(format12h)