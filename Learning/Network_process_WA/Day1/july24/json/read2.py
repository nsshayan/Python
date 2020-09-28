from pickle import loads
import sys

data = sys.stdin.read()

a = loads(data)
#b = loads(data)
#c = loads(data)

a.drive()
#b.drive()
#print c

