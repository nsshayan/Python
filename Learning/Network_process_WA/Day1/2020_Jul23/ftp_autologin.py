import pexpect

log = open("ftp_pexpect.log", "ab")

ftp = pexpect.spawn("ftp ftp.chandrashekar.info", logfile=log)
ftp.expect(b"Name .*: ")
ftp.sendline(b"testuser")

ftp.expect(b"Password: ")
ftp.sendline(b"w3lc0me")

ftp.expect(b"ftp> ")
ftp.sendline(b"cd /www/files")

ftp.expect(b"ftp> ")
ftp.sendline(b"")
ftp.interact()
print("Back to program..")
#ftp.sendline("cd /www/files/python")

#ftp.expect("ftp> ")
#ftp.sendline("get userdb.py")

#ftp.expect("ftp> ")
# ftp.sendline("quit")

ftp.close()
