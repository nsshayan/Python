from pssh.clients import ParallelSSHClient

hosts = ['192.168.56.101', "localhost"]
client = ParallelSSHClient(hosts, user="root", password="welcome")
output = client.run_command('ls /usr/local/src')

for host, host_output in output.items():
    for line in host_output.stdout:
        print(f"Host [{host}] - {line}")
