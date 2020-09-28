from pssh.clients import SSHClient

client = SSHClient("192.168.56.101", user="root", password="welcome")
client.copy_remote_file('/etc/passwd', 'p.txt')
