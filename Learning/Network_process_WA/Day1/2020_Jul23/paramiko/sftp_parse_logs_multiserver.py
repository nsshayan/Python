#!/usr/bin/env python
from gevent import monkey; monkey.patch_all()

from threading import Thread
from ssh_connection import *

parse_servers = {
    "192.168.56.101" : {
            "username": "root",
            "password": "welcome",
            "files": {
                "/var/log/system.log": r"(\d+)(\.\d+){3}",
                "/var/log/pacman.log": r"install",
            }
    },        
    
    "192.168.56.102" : {
            "username": "root",
            "password": "welcome",
            "files": {
                "/var/log/system.log": r"(\d+)(\.\d+){3}",
                "/var/log/pacman.log": r"install",

            }
    },        
    
        
        
}


def parse_logfiles(sftp, host, info, out):
    import re
    for filepath, regex in info["files"].items():
        pattern = re.compile(regex)
        with sftp.open(filepath) as logfile:
            for line in logfile:
                if pattern.search(line):
                    print("{}:{}:{}".format(host, filepath, line), file=out)

def process_server(host, info, out):
    ssh = ssh_connect(host, info["username"], info["password"])
    parse_logfiles(ssh.open_sftp(), host, info, out)
            
def parse_logs(server_config, out):
    from ssh_connection import ssh_connect, ssh_close
    workers = []
    for servername, serverinfo in server_config.items():
        #process_server(servername, serverinfo, out)
        t = Thread(target=process_server, args=(servername, serverinfo, out))
        t.start()
        workers.append(t)
        
if __name__ == '__main__':
    import sys
    
    parse_logs(parse_servers, out=sys.stdout)

