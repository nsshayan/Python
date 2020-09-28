#!/usr/bin/env python

from paramiko import SSHClient, AutoAddPolicy


ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect("192.168.56.101", username="root", password="welcome")

sftp = ssh.open_sftp()

sftp.mkdir("/tmp/scripts")

sftp.put("get_ip_linux.py", "/tmp/scripts/get_ip.py")

stdin, stdout, stderr = ssh.exec_command("python /tmp/scripts/get_ip.py")
print(stdout.read())

sftp.unlink("/tmp/scripts/get_ip.py")
sftp.rmdir("/tmp/scripts")


sftp.close()
ssh.close()
