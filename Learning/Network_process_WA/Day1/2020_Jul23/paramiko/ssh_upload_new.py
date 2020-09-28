#!/usr/bin/env python
"""
Exercise:
=========
Write a program to upload a directory tree
to a remote server via SSH.

Example usage:
--------------
    $ ./ssh_upload.py
    usage: ./ssh_upload.py local-path user@hostname:remote-path

    $ ./ssh_upload.py samples root@192.168.56.101:~/test_folder


Download this code snippet from the following URL:
    https://public.etherpad-mozilla.org/p/Advanced_Python

"""

def ssh_connect(host, username, password):
    from paramiko import SSHClient, AutoAddPolicy
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(host, username=username, password=password)
    return client

def upload(ssh_client, source_path, dest_path):
    remote_command = "mkdir -p {0}; cd {0}; tar xf - >/dev/null 2>&1"

    transport = ssh_client.get_transport()

    channel = transport.open_channel("session")
    #channel.exec_command("cat > test.tar")
    channel.exec_command(remote_command.format(dest_path))
    #channel.exec_command("cat | ./get_tar.py")

    stream = channel.makefile("wb")

    from tarfile import TarFile
    tar_stream = TarFile(fileobj=stream, mode="w")
    tar_stream.add(source_path)

    tar_stream.close()
    channel.close()
    ssh_client.close()

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
            "local_path",
            help="Path to local directory")
    parser.add_argument(
            "remote_path",
            help="Path to remote location in the form 'user@remotehost:/path'")

    args = parser.parse_args()

    import re
    pattern = re.compile(r'^(\w+)@([\w\.]+):(.+)$')
    match = pattern.search(args.remote_path)
    if not match or len(match.groups()) != 3:
        print("Error: remote_path format is incorrect!")
        exit(1)
    else:
        username, host, dest_path = match.groups()
    from getpass import getpass
    password = getpass("Enter password: ")

    import logging
    logging.basicConfig(filename="ssh_upload.log")
    log = logging.getLogger("paramiko")
    log.setLevel(logging.DEBUG)

    ssh_client = ssh_connect(host, username, password)
    upload(ssh_client, args.local_path, dest_path)


