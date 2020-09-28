from paramiko import SSHClient, AutoAddPolicy

import logging
logging.basicConfig(filename="run_bc.log")
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
stdin, stdout, stderr = client.exec_command('bc')
stdin.write(commands)

# for line in stdout:
#    print('... ' + line.strip('\n'))
data = stdout.readlines()

client.close()
for line in data:
    print(line.strip())
