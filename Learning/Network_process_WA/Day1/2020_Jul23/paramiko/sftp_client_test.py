def sftp_client_from_transport(hostname, username, password):
    from paramiko import Transport
    tn = Transport((hostname, 22))
    tn.connect(username=username, password=password)
    return tn.open_sftp_client()


def sftp_client_from_transport_old(hostname, username, password):
    from paramiko import Transport, SFTPClient
    tn = Transport((hostname, 22))
    tn.connect(username=username, password=password)
    return SFTPClient.from_transport(tn)


def sftp_client_from_ssh_client(hostname, username, password):
    from paramiko import SSHClient, AutoAddPolicy

    sshclient = SSHClient()
    sshclient.set_missing_host_key_policy(AutoAddPolicy())
    sshclient.connect(hostname, username=username, password=password)

    return sshclient.open_sftp()


if __name__ == '__main__':
    sftp = sftp_client_from_transport("192.168.56.101", "root", "welcome")

    print(sftp.listdir("/"))         # Listing contents of a directory
    sftp.mkdir("/tmp/testfolder")    # Create a new directory
    sftp.chdir("/tmp/testfolder")    # Change directory
    print(sftp.getcwd())             # Get current working directory
    sftp.chdir("..")
    sftp.rmdir("/tmp/testfolder")  # Remote directory

    # Upload file
    local_file = "a.json"
    remote_path = "/tmp/testfile.json"
    r = sftp.put(local_file, remote_path)  # Upload local_file to remote_path
    print(r)  # Attributes of remotely created file
    print(sftp.listdir("/tmp"))

    # Download file
    remote_path = "/etc/passwd"
    local_path = "./testfile.txt"
    sftp.get(remote_path, local_path)
    import os
    print(os.listdir("."))

    # Delete a remote file
    sftp.unlink("/tmp/testfile.json")
    print(sftp.listdir("/tmp"))
