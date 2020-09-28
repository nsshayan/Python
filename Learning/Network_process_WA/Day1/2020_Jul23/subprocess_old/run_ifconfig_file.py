from subprocess import Popen, PIPE

with open("ipaddress.txt", "w") as out:
    p = Popen(["/sbin/ifconfig"], stdout=out)


