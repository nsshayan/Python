from subprocess import Popen, PIPE

process = Popen(["ls",  "-l"])
print("ls command running...")
ret = process.wait()
print(("ls returned ", ret))

