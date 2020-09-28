from paramiko import SSHClient, WarningPolicy

client = SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(WarningPolicy())

commands = """
scale=1000
sqrt(2)
quit
"""

client.connect('192.168.56.101', username='chandra', password='welcome')
stdin, stdout, stderr = client.exec_command('bc')
stdin.write(commands)

#for line in stdout:
#    print('... ' + line.strip('\n'))
data = stdout.readlines()

client.close()
print(data)

