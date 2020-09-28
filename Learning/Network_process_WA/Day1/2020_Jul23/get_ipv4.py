from subprocess import Popen, PIPE

#p = Popen("ifconfig", stdout=PIPE, universal_newlines=True) # Python 3.3+
p = Popen("ifconfig", stdout=PIPE, encoding="utf8") # Python 3.6+

for line in p.stdout:
    #print(line)
    #if b"inet " in line:
     #   print(str(line.split()[1], "utf8"))

    if "inet " in line:
        print(line.split()[1])