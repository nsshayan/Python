import os

print("Launching ls...")
ret = os.system("ls > ls.out")
print("Command complete: ret =", ret)

