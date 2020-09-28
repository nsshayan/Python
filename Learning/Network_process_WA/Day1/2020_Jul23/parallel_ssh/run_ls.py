from pssh.clients import SSHClient

host = '192.168.56.101'
client = SSHClient(host, user="root", password="welcome")
channel, host, stdout, stderr, stdin  = client.run_command('ls /usr/local/src')

for line in stdout:
    print(line)
