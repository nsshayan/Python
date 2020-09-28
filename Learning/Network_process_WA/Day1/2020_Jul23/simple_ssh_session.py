from paramiko import SSHClient, AutoAddPolicy, RejectPolicy, WarningPolicy

client = SSHClient()
client.load_system_host_keys()

#client.set_missing_host_key_policy(RejectPolicy())
client.set_missing_host_key_policy(AutoAddPolicy())
#client.set_missing_host_key_policy(WarningPolicy())

client.connect("192.168.56.105", username="root", password="welcome")

stdin, stdout, stderr = client.exec_command("uname -r")
for line in stdout:
    print(line)

commands = ["date", "hostname", "whoami", "id", "exit"]
channel = client.invoke_shell()
stdin = channel.makefile("w")
stdout = channel.makefile("r")
stderr = channel.makefile_stderr("r")

for c in commands:
    stdin.write(c + "\n")

for line in stdout:
    print(line)

client.close()
