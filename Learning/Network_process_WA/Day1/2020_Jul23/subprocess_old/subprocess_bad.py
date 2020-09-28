def Popen(x):
    print("Popen called with", x)
    return 0

from subprocess import Popen

p = Popen("ls")

