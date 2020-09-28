from sys import argv
from ftplib import FTP
import os

if len(argv) < 3:
    print("usage: {} local-folder remotesite/remotepath".format(argv[0]))
    exit(1)

local_path = argv[1]
host, remote_path = argv[2].split("/", 1)
remote_path = "/" + remote_path

ftp = FTP(host, "testuser", "w3lc0me")
ftp.cwd(remote_path)
ftp.mkd(remote_path + "/" + local_path)
print("Connecting to {} and changing to {}".format(host, remote_path))

for path, dirs, files in os.walk(local_path):
    #print("Path: {}, dirs = {}, files = {}".format(path, dirs, files))
    #print("-" * 50)

    print("Changing directory to", path)
    ftp.cwd(remote_path + "/" + path)

    for d in dirs:
        print("Creating directory ", d)
        ftp.mkd(d)

    for source_file in files:
        print("Uploading file ", source_file)
        with open(path + "/" + source_file, "rb") as source:
            ftp.storbinary("STOR " + source_file, source)




