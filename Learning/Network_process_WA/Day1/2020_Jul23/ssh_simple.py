import paramiko
from getpass import getpass

passphrase = getpass("Enter passphrase to connect to servers: ")

client = paramiko.SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

client.connect("192.168.56.101", username="root", password=passphrase)

commands = """
scale=1000
4*a(1)
quit
"""

stdin, stdout, stderr = client.exec_command("bc -l")

stdin.write(commands)
stdin.close()

for line in stdout:
    print(line)
