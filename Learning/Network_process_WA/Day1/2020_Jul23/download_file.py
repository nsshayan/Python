import pexpect

ftp = pexpect.spawn("ftp ftp.chandrashekar.info")

ftp.expect(r"Name .+: ")
ftp.sendline("testuser")

print("before =", ftp.before)
print("after =", ftp.after)


ftp.expect(r"Password: ")
ftp.sendline("w3lc0me")

ftp.expect("ftp> ")
ftp.sendline("cd /www/files")

ftp.expect("ftp> ")
ftp.sendline("binary")

ftp.expect("ftp> ")
ftp.sendline("passive")

ftp.expect("ftp> ")
ftp.sendline("get xml.zip")

ftp.expect("ftp> ")
ftp.sendline("quit")


