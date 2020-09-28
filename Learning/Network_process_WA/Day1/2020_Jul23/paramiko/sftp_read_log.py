#!/usr/bin/env python
import paramiko
import re


def parse_file(client, filename, pattern, process):
    with client.open(filename, "r") as infile:
        for line in infile:
            matches = pattern.finditer(line)
            if matches:
                for match in matches:
                    process(match)


def print_block(m):
    print(m.groupdict())
    print(m.group())


blocks = re.compile(r"\[sda\]\s+(?P<blocksize>\d+)")

t = paramiko.Transport(("192.168.56.101", 22))
t.connect(username="root", password="welcome")
sftp = paramiko.SFTPClient.from_transport(t)

parse_file(sftp, "/var/log/system.log", blocks,  print_block)


sftp.close()
t.close()
