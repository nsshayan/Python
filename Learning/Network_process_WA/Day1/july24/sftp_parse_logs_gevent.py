#!/usr/bin/env python
from gevent import monkey; monkey.patch_all()
import gevent
import paramiko
import re

servers = {
    "192.168.56.101": {"username": "root",
                       "password": "welcome",
                       "files": ("/var/log/system.log", "/var/log/pacman.log")
    },

    "192.168.1.150": {"username": "testuser",
                       "password": "welcome",
                       "files": ("/root/test.log",)
    }
}

clients = { }

def parse_file(client, filename, pattern, process):
    with client.open(filename, "r") as infile:
        for line in infile:
            if pattern.search(line): process(line)

ip_addr = re.compile(r"\d+")


def create_connection(hostname, username, password):
    transport = paramiko.Transport((hostname, 22))
    transport.connect(username=username, password=password)
    clients[k] = {}
    clients[k]["connection"] = paramiko.SFTPClient.from_transport(transport)
    clients[k]["files"] = v["files"]


try:
    for k, v in servers.items():


    pool = []
    for k, v in clients.items():
        for f in v["files"]:
            t = gevent.spawn(parse_file, v["connection"], f, ip_addr, print)
            pool.append(t)


    gevent.joinall(pool)

finally:
    for k, v in clients.items(): v["connection"].close()
