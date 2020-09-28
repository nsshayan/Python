#!/usr/bin/env python

import paramiko


t = paramiko.Transport(("192.168.56.101", 22))
t.connect(username="root", password="welcome")

sftp = paramiko.SFTPClient.from_transport(t)

with sftp.open("/etc/vimrc") as log:
    for line in log:
            print(line.upper())


sftp.close()
t.close()
