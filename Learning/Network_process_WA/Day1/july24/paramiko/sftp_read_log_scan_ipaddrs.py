#!/usr/bin/env python
from ssh_connection import *

import re

ip_addr = re.compile(r"\d{1,3}(\.\d{1,3}){3}")

ssh_client = ssh_connect("192.168.56.101", username="root")
sftp = ssh_client.open_sftp()

with sftp.open("/var/log/system.log", "r") as logfile:
    for line in logfile:
        if ip_addr.search(line):
            print(line)
sftp.close()
ssh_client.close()
