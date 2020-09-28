from paramiko import SSHClient, AutoAddPolicy

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())

client.connect("192.168.56.105", username="root", password="welcome")

stdin, stdout, stderr = client.exec_command("ls -l /usr/local")

for line in stdout:
    print(line)

client.close()
