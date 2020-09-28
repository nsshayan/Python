import pexpect

ftp = pexpect.spawn("ftp ftp.chandrashekar.info", encoding="utf8")

ftp.expect("Name.+:")
ftp.sendline("testuser")

ftp.expect("Password:")
ftp.sendline("w3lc0me")

ftp.expect("ftp>")
ftp.sendline("cd /www/files")

ftp.expect("ftp>")
ftp.sendline("bin")

ftp.expect("ftp>")
ftp.sendline("get xml.zip")

ftp.expect("ftp>")
ftp.sendline("quit")

ftp.close()
