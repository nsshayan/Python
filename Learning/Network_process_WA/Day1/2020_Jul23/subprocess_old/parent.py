import os

print("Process id = ", os.getpid())

#os.execve("./child.py", ["./child.py"], os.environ)

os.system("./child.py")

print("Back to parent process, pid =", os.getpid())

