#!/usr/bin/env python

import paramiko
import re

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('192.168.56.101', username='chandra', password="welcome")

transport = client.get_transport()
channel = transport.open_channel("session")

with open("a.txt", "rb") as f:
    channel.exec_command('cat > test.txt')
    channel.send(f.read())

channel.close()

client.close()
