#!/usr/bin/env python
import logging

import paramiko
from subprocess import Popen, PIPE
from time import sleep

logging.basicConfig(filename="ssh_upload.log")
log = logging.getLogger("paramiko")
log.setLevel(logging.DEBUG)

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('192.168.56.101', username='root', password="welcome")

transport = client.get_transport()
channel = transport.open_channel("session")

channel.exec_command('cat > test.tar')
tar_command = Popen(["tar", "c", "test"], stdout=PIPE)
output = channel.makefile("wb")
output.write(tar_command.stdout.read())
tar_command.wait()
output.close()
channel.close()

client.close()
