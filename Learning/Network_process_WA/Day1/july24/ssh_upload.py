#!/usr/bin/env python

import paramiko
from subprocess import Popen, PIPE

#client = paramiko.SSHClient()
#client.load_system_host_keys()
#client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#client.connect('192.168.56.101', username='testuser', password="welcome")
#transport = client.get_transport()

transport = paramiko.Transport(("192.168.56.101", 22))
transport.connect(username="testuser", password="welcome")

channel = transport.open_channel("session")

tar_input_stream = Popen(["tar", "c", "2017_May25"], stdout=PIPE)
channel.exec_command('tar x')
#channel.send(tar_input_stream.stdout.read())
BLOCK_SIZE = 8192
while True:
   block = tar_input_stream.stdout.read(BLOCK_SIZE)
   if not block: break
   channel.send(block)

tar_input_stream.wait()

channel.close()

client.close()
