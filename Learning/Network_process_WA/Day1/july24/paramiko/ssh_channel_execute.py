def ssh_connect(host, username, password):
    from paramiko import SSHClient, AutoAddPolicy
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(host, username=username, password=password)
    return client

def transport_connect(host, username, password):
    from paramiko import Transport

    t = Transport((host, 22))
    t.connect(username=username, password=password)
    return t

def sftp_from_transport(host, username, password):
    from paramiko import SFTPClient
    transport = transport_connect(host, username, password)
    #sftp = SFTPClient.from_transport(transport)
    sftp = transport.open_sftp_client()
    return sftp

def sftp_from_sshclient(host, username, password):
    client = ssh_connect(host, username, password)
    sftp = client.open_sftp()
    return sftp

if __name__ == '__main__':
#    client = ssh_connect("192.168.56.101", "root", "welcome")
#    channel = client.get_transport().open_channel("session")
    transport = transport_connect("192.168.56.101", "root", "welcome")
    channel = transport.open_channel("session")
    channel.exec_command("dmesg")
    stream = channel.makefile("r")
    for line in stream:
        print(line)