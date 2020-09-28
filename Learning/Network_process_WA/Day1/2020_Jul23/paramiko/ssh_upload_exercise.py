#!/usr/bin/env python
"""
Exercise:
=========
Write a program to upload a directory tree (recursively)
to a remote server via SSH.

Example usage:
--------------
    $ ./ssh_upload.py
    usage: ./ssh_upload.py local-path user@hostname:remote-path

    $ ./ssh_upload.py samples/ root@192.168.56.101:~/test_folder


Download this code snippet from the following URL:
    https://public.etherpad-mozilla.org/p/advanced_python

Hint: Lookup tarfile module in python and find out how to
tar a directory structure and stream via SSH to 'tar' command
on the remote machine which is configured to extract this data.

On Unix/Linux command-line using openssh client, the equivalent
command would be as below:
    tar c xml | ssh root@192.168.56.101 "tar xf - 2>/dev/null"

"""

def ssh_connect(host, username, password):
    pass # TODO: Implement this function

def upload(ssh_client, source_path, dest_path):
    pass # TODO: Implement this function

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

    # TODO: Implement the following functions...
    ssh_client = ssh_connect(host, username, password)
    upload(ssh_client, args.local_path, dest_path)


