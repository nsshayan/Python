import pexpect

log = open("ftp_pexpect.log", "a")

ftp = pexpect.spawn("ftp ftp.chandrashekar.info", logfile=log)
ftp.expect("Name .*: ")
ftp.sendline("testuser")

ftp.expect("Password: ")
ftp.sendline("w3lc0me")

ftp.expect("ftp> ")
ftp.sendline("cd /www/files/python")

ftp.expect("ftp> ")
ftp.sendline("get userdb.py")

ftp.expect("ftp> ")
ftp.sendline("quit")

ftp.close()

