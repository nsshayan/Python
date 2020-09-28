from subprocess import Popen

with open("outfile.txt", "w") as outfile:
    p = Popen("ifconfig", stdout=outfile)
    r = p.wait()
    print("Program exited with return code", r)



