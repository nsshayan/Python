from paramiko import SSHClient, AutoAddPolicy
import logging
logging.basicConfig(filename="run_multiple_commands.log")
log = logging.getLogger("paramiko")
log.setLevel(logging.DEBUG)

client = SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy())

commands = """
scale=1000
sqrt(2)
quit
"""

client.connect('192.168.56.101', username='root', password='welcome')
#stdin, stdout, stderr = client.exec_command('cd /etc')

#stdin, stdout, stderr = client.exec_command("pwd")
#data = stdout.readlines()
#print(data)


stdin, stdout, stderr = client.exec_command("/bin/bash -c 'cd /etc; pwd'")

output = stdout.readlines()
print(output)

client.close()

