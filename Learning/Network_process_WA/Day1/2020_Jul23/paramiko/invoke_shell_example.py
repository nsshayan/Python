from paramiko import SSHClient, AutoAddPolicy

client = SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy())

client.connect('192.168.56.101', username='root', password='welcome')

ch = client.invoke_shell()
stdout = ch.makefile("r")
stdin = ch.makefile("w")
stderr = ch.makefile_stderr("r")

stdin.write("echo $$\n")
print(stdout.readline())
client.close()
