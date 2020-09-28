from subprocess import Popen

with open("lsoutput.txt", "wb") as outfile:
    p = Popen("ls", stdout=outfile)
    p.wait()
