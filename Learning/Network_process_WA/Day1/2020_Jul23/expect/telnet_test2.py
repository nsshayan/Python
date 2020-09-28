import pexpect
from time import sleep

child = pexpect.spawn('telnet -l pythonista 192.168.56.101',
                       logfile=open("log.txt", "wb"))

#child.expect('login: ')
#child.sendline('joe')

prompt = r"\[pythonista@archvm ~\]\$"

sleep(2)
child.expect('Password: ')

child.sendline('welcome')

child.expect(prompt)
child.sendline('uname -a; date; whoami; id; w')
child.expect(prompt)

print(str(child.before, "utf8"))

child.sendline('exit')
