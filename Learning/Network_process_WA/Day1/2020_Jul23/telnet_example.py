import pexpect
from time import sleep

log = open("telnet_pexpect.log", "a")
telnet = pexpect.spawn("telnet -l pythonista 192.168.56.101", logfile=log, encoding="utf8", timeout=300)

sleep(1)
telnet.expect("Password: ")
sleep(1)
telnet.sendline("welcome123")

telnet.expect("\[pythonista@archvm ~\]\$ ")
#telnet.sendline("uname -a")
telnet.sendline("ifconfig")
telnet.expect("\[pythonista@archvm ~\]\$ ")

#print(telnet.before)
for line in telnet.before.splitlines():
    if "inet " in line:
        print(line.split()[1])
telnet.close()
