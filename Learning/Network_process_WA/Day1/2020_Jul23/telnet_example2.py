import pexpect
from time import sleep

log = open("telnet_pexpect.log", "a")
telnet = pexpect.spawn("telnet -l root 192.168.56.101", logfile=log, encoding="utf8", timeout=300)

sleep(1)
telnet.expect("Password: ")
sleep(1)
telnet.sendline("welcome")

telnet.expect("\[root@archvm ~\]# ")
telnet.sendline("ls")
telnet.expect("\[root@archvm ~\]# ")
print("Output of ls: ", telnet.before)

telnet.sendline("whoami")
telnet.expect("\[root@archvm ~\]# ")
print("Output of whoami: ", telnet.before)


telnet.close()

