from paramiko import SSHClient, AutoAddPolicy
from threading import Thread
import rlcompleter
from collections import deque

def send_commands(outstream):
    while True:
        command = input("Cmd> ")
        if command == "exit":
            outstream.close()
            break
        print(command, file=outstream)

def get_output(instream):
    for line in instream:
        print(line, end="")


ssh_client = SSHClient()
ssh_client.set_missing_host_key_policy(AutoAddPolicy())
ssh_client.connect(
    hostname="dhrona.net",
    username="user1",
    password="welcome",
    port=12276)

client_channel = ssh_client.invoke_shell()

stdin, stdout, stderr = (client_channel.makefile("w"),
                         client_channel.makefile("r"),
                         client_channel.makefile_stderr("r"))


command_thread = Thread(target=send_commands, args=(stdin,))
stdout_thread = Thread(target=get_output, args=(stdout,))
stderr_thread = Thread(target=get_output, args=(stderr,))

threads = deque([command_thread, stdout_thread, stderr_thread])

for t in threads:
    t.start()

while threads:
    t = threads[0]
    t.join(1)
    if not t.is_alive():
        threads.popleft()
    else:
        threads.rotate(-1)
