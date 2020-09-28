from subprocess import Popen, PIPE

p = Popen(["ipconfig"], stdout=PIPE)

#for line in p.stdout:
#    if "IPv4 Address" in line:
#        print line.split(":")[-1].strip()

print([ line.split(":")[-1].strip() for line in p.stdout if "IPv4 Address" in line ]) 

