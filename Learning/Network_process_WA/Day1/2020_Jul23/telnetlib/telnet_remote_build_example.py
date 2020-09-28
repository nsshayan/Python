import sys
from telnetlib import Telnet
import re
from time import sleep

HOST = "192.168.56.101"
PORT = 2023
user = b"pythonista\r"
password = b"welcome\r"
shell_prompt = b"]$ "

tn = Telnet(HOST, PORT)
#tn.set_debuglevel(7)

def send_shell_command(c):
    tn.write(bytes(c + "\n", "utf8"))
    return str(tn.read_until(shell_prompt), "utf8")

def login(username, password):
    tn.read_until(b"login: ")
    tn.write(username)

    tn.read_until(b"Password:")
    tn.write(password)
    return str(tn.read_until(shell_prompt), "utf8")

login(user, password)
print(send_shell_command("screen"))
tn.write(b"\x01H")
sleep(0.01)
print(send_shell_command("mkdir ~/build"))
print(send_shell_command("cp /boot/config-4.9.0-vbox ~/build/.config"))
print(send_shell_command("cd /usr/local/src/linux-4.9.0"))
tn.write(b"make O=/home/pythonista/build\n")
sleep(0.01)
tn.write(b"\x01\x04")

print(str(tn.read_until(shell_prompt), "utf8"))

print(send_shell_command("exit"))

