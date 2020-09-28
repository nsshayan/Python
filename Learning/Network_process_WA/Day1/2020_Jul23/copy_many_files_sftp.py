import paramiko
from glob import glob

t = paramiko.Transport(("192.168.56.101", 22))
t.connect(username="root", password="welcome")
sftp = paramiko.SFTPClient.from_transport(t)

sftp.mkdir("paramiko")

for file in glob("paramiko/*"):
    sftp.put(file, file)

sftp.close()

