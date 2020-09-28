from paramiko import SSHClient, AutoAddPolicy, RejectPolicy, WarningPolicy
import rlcompleter
from threading import Thread

def input_loop(stream):
    quit = False
    while not quit:
        command = input("SSH> ")
        if command == "exit":
            quit = True
        stream.write(command + "\n")
        stream.flush()
    stream.close()

results = []
def output_loop(stream):
    for line in stream:
        results.append(line)
        print(line)

client = SSHClient()
client.load_system_host_keys()

#client.set_missing_host_key_policy(RejectPolicy())
client.set_missing_host_key_policy(AutoAddPolicy())
#client.set_missing_host_key_policy(WarningPolicy())

client.connect("192.168.56.105", username="root", password="welcome")

channel = client.invoke_shell()
stdin = channel.makefile("w")
stdout = channel.makefile("r")
stderr = channel.makefile_stderr("r")

input_thread = Thread(target=input_loop, args=(stdin,))
output_thread = Thread(target=output_loop, args=(stdout,))
error_thread = Thread(target=output_loop, args=(stderr,))

input_thread.start()
output_thread.start()
error_thread.start()

input_thread.join()
client.close()
print("------------------- final output ------------------")
print("".join(results))