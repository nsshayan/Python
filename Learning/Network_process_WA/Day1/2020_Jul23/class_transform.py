class Car: pass

c = object()
c.__class__ = Car

print(c)
