from subprocess import Popen, PIPE

p = Popen("/sbin/ifconfig",
          #universal_newlines=True,
          encoding="utf8",
          stdout=PIPE)

#for line in p.stdout:
#    if "inet " in line:
#        print(line.split()[1])

ipaddrs = [ line.split()[1] for line in p.stdout \
             if "inet " in line]

print(ipaddrs)

