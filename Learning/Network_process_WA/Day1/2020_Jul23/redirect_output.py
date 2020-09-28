from subprocess import Popen

with open("ifconfig.log", "wb") as outfile:
    p = Popen("ifconfig", stdout=outfile)
    p.wait()
