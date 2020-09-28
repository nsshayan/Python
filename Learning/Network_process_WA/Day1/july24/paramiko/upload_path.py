#!/usr/bin/env python

import paramiko
from subprocess import Popen, PIPE

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('192.168.56.101', username='root', password="welcome")

transport = client.get_transport()
channel = transport.open_channel("session")

tar_command = Popen("tar c paramiko", stdout=PIPE)

channel.exec_command('tar x')
channel.send(tar_command.stdout)

channel.close()

client.close()
