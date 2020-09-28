import paramiko

import logging
logging.basicConfig(filename="run_ls.log")
log = logging.getLogger("paramiko")
log.setLevel(logging.DEBUG)

#key = paramiko.RSAKey(data=base64.decodestring('AAA...'))
#client.get_host_keys().add('ssh.example.com', 'ssh-rsa', key)

client = paramiko.SSHClient()
# client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.set_missing_host_key_policy(paramiko.RejectPolicy())
# client.set_missing_host_key_policy(paramiko.WarningPolicy())

#from getpass import getpass
#password = getpass("Enter password: ")

#password = "welcome"

client.connect('192.168.56.101', username="root")
stdin, stdout, stderr = client.exec_command("./long_script.py")
for line in stdout:
    print('... ' + line.strip('\n'))
client.close()
