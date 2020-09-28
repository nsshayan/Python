from subprocess import Popen, PIPE

with open("ls.out", "w") as outfile:
    p = Popen("ls", stdout=outfile, universal_newlines=True) # 3.2+
    #p = Popen("ls", stdout=outfile, encoding="utf8") # 3.5+
