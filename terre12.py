# 12 TO 24

import sys
import datetime as dt

input = sys.argv[1]
format12h = dt.datetime.strptime(input, '%I:%M%p')
format24h = dt.datetime.strftime(format12h, '%H:%M')


print(format24h)