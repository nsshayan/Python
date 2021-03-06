#!/usr/bin/env python
"""
Exercise:
=========
Write a program to upload a directory tree
to a remote server via SSH.

Example usage:
--------------
    $ ./sftp_upload.py
    usage: ./sftp_upload.py local-path user@hostname:remote-path

    $ ./sftp_upload.py samples root@192.168.56.101:~/test_folder


Download this code snippet from the following URL:
    https://public.etherpad-mozilla.org/p/advanced_python

"""

def ssh_connect(host, username, password):
    from paramiko import SSHClient, AutoAddPolicy
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(host, username=username, password=password)
    return client

def upload(ssh_client, source_path, dest_path):
    sftp = ssh_client.open_sftp()
    #TODO: Implement the logic here!

def parse_arguments():
    program_help = """
    Upload a directory tree to a remote machine via SFTP protocol.

    Usage:
        $ ./sftp_upload.py local_path remote_user@hostname:remote_path

    Example:
        $ ./sftp_upload.py samples root@192.168.56.101:~/test_folder
    """

    from argparse import ArgumentParser

    parser = ArgumentParser(description=program_help)
    parser.add_argument(
            "local_path",
            help="Path to local directory")
    parser.add_argument(
            "remote_path",
            help="Path to remote location in the form 'remote_user@remote_host:/remote_path'")

    return parser.parse_args()

def parse_destination(remote_path):
    import re
    pattern = re.compile(r'^(\w+)@([\w\.]+):(.+)$')
    match = pattern.search(remote_path)
    if not match or len(match.groups()) != 3:
        raise ValueError("Error: remote_path format is incorrect!")
    else:
        return match.groups()

def setup_logging():
    import logging
    logging.basicConfig(filename="sftp_upload.log")
    log = logging.getLogger("paramiko")
    log.setLevel(logging.DEBUG)


if __name__ == '__main__':
    args = parse_arguments()

    try:
        username, host, dest_path = parse_destination(args.remote_path)
    except ValueError as e:
        print(e)
        exit(1)

    from getpass import getpass
    password = getpass("Enter password: ")

    setup_logging()
    ssh_client = ssh_connect(host, username, password)
    upload(ssh_client, args.local_path, dest_path)
