#!/usr/bin/env python

import paramiko

#from getpass import getpass

#uname = input("Enter username: ")
#passwd = getpass("Enter password: ")

t = paramiko.Transport(("192.168.56.101", 22))
#t.connect(username=uname, password=passwd)

t.connect(username="root", password='welcome')
sftp = paramiko.SFTPClient.from_transport(t)

#client = paramiko.SSHClient()
#client.load_system_host_keys()
#client.set_missing_host_key(paramiko.AutoAddPolicy())
#client.connect(username="root", password="welcome")

#sftp = paramiko.SFTPClient.from_transport(client.get_transport())
#sftp = client.open_sftp()

#sftp.mkdir("/root/this-is-a-test-folder")
sftp.chdir("/root/this-is-a-test-folder")
dirlist = sftp.listdir('.')
print("Dirlist:", dirlist)

with sftp.open("a.txt", "wb") as outfile:
    outfile.write("this is a test string\n")

dirlist = sftp.listdir('.')
print("Dirlist:", dirlist)

with sftp.open("a.txt", "rb") as infile:
    print(infile.read())

sftp.put("sftp_upload_file.py", "testfile.py")
dirlist = sftp.listdir('.')
print("Dirlist:", dirlist)

sftp.get("/etc/passwd", "p.txt")

sftp.unlink("testfile.py")
dirlist = sftp.listdir('.')
print("Dirlist:", dirlist)

#sftp.put("run_ls.py", "/tmp/aaaabbbbcccc.txt")
#with sftp.open("/tmp/a.dat", "w") as out:
#    with open("../../system.log") as src:
#        while True:
#            block = src.read(8192)
#            if not block: break
#            out.write(block)




# sftp.get("remotefile", "localfile")
# sftp.mkdir("remote-dir")
# sftp.open("remote-file", "w").write("this is a new file\n")
# print sftp.open("remote-file", "r").read()


#sftp.close()
t.close()
