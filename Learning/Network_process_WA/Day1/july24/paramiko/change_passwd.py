from paramiko import SSHClient, AutoAddPolicy

client = SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy())


client.connect('192.168.56.101', username='root', password='welcome')
stdin, stdout, stderr = client.exec_command('passwd chandra')
stdin.write("python123\n")
stdin.flush()
stdin.write("python123\n")
stdin.flush()

data = stdout.readlines()

client.close()
print(data)

