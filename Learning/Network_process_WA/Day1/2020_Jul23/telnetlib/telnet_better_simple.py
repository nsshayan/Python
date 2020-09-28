from telnetlib import Telnet
from time import sleep

HOST = "192.168.56.101"
user = b"root"
password = b"welcome" 

shell_prompt = b"[root@archvm ~]# "

commands = [
    (b"login",  user),
    (b"Password", password),
    (shell_prompt, [b"whoami", b"uname -a", b"ls /etc", b"exit"])
]

def run_commands(host, commands):
    output = []
    for prompt, cmd in commands:
        if type(cmd) is bytes:
            output.append(str(host.read_until(prompt), "utf8"))
            host.write(cmd + b"\r")
        elif type(cmd) is list:
            for c in cmd:
                output.append(str(host.read_until(prompt), "utf8"))
                host.write(c + b"\r")
    return output

tn = Telnet(HOST)
out = run_commands(tn, commands)
for o in out:
    print(o)
    print("----------------------------------")


