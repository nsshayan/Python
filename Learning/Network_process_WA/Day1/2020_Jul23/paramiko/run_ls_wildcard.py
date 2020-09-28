import paramiko

#key = paramiko.RSAKey(data=base64.decodestring('AAA...'))
#client.get_host_keys().add('ssh.example.com', 'ssh-rsa', key)

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#client.set_missing_host_key_policy(paramiko.RejectPolicy())
#client.set_missing_host_key_policy(paramiko.WarningPolicy())

#from getpass import getpass
#password = getpass("Enter password: ")

password = "welcome"

client.connect('192.168.56.101', username='root', password=password)
stdin, stdout, stderr = client.exec_command('ls /etc/*.conf')
for line in stdout:
    print('... ' + line.strip('\n'))
client.close()
