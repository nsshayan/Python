#!/usr/bin/env python

import paramiko
import re
from threading import Thread

servers = {
    "192.168.56.101": {"username": "root",
                       "password": "welcome",
                       "files": ("/var/log/system.log", "/var/log/pacman.log")
                       },

    "192.168.56.102": {"username": "root",
                       "password": "welcome",
                       "files": ("/root/test.log",)
                       }
}

clients = {}


def parse_file(client, filename, pattern, process):
    with client.open(filename, "r") as infile:
        for line in infile:
            if pattern.search(line):
                process(line)


ip_addr = re.compile(r"(\d{1,3})(\.\d{1,3}){3}")

try:
    for k, v in servers.items():
        transport = paramiko.Transport((k, 22))
        transport.connect(username=v["username"], password=v["password"])
        clients[k] = {}
        clients[k]["connection"] = paramiko.SFTPClient.from_transport(
            transport)
        clients[k]["files"] = v["files"]

    pool = []
    for k, v in clients.items():
        for f in v["files"]:
            t = Thread(target=parse_file,
                       args=(v["connection"], f, ip_addr, print))
            pool.append(t)
            t.start()

    for t in pool:
        t.join()

finally:
    for k, v in clients.items():
        v["connection"].close()
