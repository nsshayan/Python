import pexpect
from time import sleep

child = pexpect.spawn('telnet -l pythonista 192.168.56.101',
                       logfile=open("log.txt", "wb"), delaybeforesend=0.5)

#child.expect('login: ')
#child.sendline('joe')

prompt = r"\[pythonista@archvm ~\]\$"

child.expect('Password: ')

sleep(0.5)
child.sendline('welcome')

child.expect(prompt)
child.sendline('uname -a')
child.expect(prompt)

print(str(child.before, "utf8"))

child.sendline("ls /etc")
child.expect(prompt)
print("=" * 50)
print(str(child.before, "utf8"))

child.sendline('exit')
