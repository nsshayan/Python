#!/usr/bin/env python


import logging
logging.basicConfig(filename="ssh_upload.log")
log = logging.getLogger("paramiko")
log.setLevel(logging.DEBUG)

import paramiko
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('192.168.56.101', username='root', password="welcome")

transport = client.get_transport()
channel = transport.open_channel("session")
#channel.exec_command("cat > test.tar")
channel.exec_command("tar xf - 2>/dev/null")
#channel.exec_command("cat | ./get_tar.py")
stream = channel.makefile("wb")

from tarfile import TarFile
tar_stream = TarFile(fileobj=stream, mode="w")
tar_stream.add("test")

tar_stream.close()
channel.close()
client.close()
