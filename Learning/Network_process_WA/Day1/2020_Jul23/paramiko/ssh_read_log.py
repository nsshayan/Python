#!/usr/bin/env python

import paramiko

remote_command = r"egrep '[0-9]{1,3}(\.[0-9]{1,3}){3}' /root/system.log"

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('192.168.56.101', username='root', password="welcome")

stdin, stdout, stderr = client.exec_command(remote_command)
for line in stdout:
    print(line)

client.close()
