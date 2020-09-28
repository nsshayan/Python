from subprocess import Popen, PIPE

#with Popen("ls", stdout=PIPE, universal_newlines=True) as p:
#with Popen("ls", stdout=PIPE) as p:
with Popen("ls", stdout=PIPE, encoding="utf8") as p:
    for line in p.stdout:
        print(line.upper())

        #print(str(line, "utf8").upper())  # Python 3.0 to 3.3