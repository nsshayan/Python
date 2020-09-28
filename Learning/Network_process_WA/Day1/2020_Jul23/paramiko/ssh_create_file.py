def ssh_connect(host, username, password):
    from paramiko import SSHClient, AutoAddPolicy
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(host, username=username, password=password)
    return client

def run_command(ssh_client):
    from sys import stdin

    remote_command = "cat > test.txt"

    transport = ssh_client.get_transport()

    channel = transport.open_channel("session")

    channel.exec_command(remote_command)

    outstream = channel.makefile("wb")

    for line in stdin:
        outstream.write(line)

    channel.close()
    ssh_client.close()


ssh_client = ssh_connect("192.168.56.101", "root", "welcome")

run_command(ssh_client)