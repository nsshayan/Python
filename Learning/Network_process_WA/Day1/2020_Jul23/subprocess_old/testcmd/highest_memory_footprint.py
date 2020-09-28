from subprocess import Popen, PIPE

p = Popen(["ps", "-aeo", "rss,pid,args"], stdout=PIPE)

#for line in p.stdout:
#    print(line.split()[0])

header = p.stdout.readline()

max_mem = max([ line.split() for line in p.stdout ])
print("Pid: {1}\nMemory usage: {0}\nCommand: {2}".format(*max_mem))

#for line in p.stdout:
#    print(line.split())


