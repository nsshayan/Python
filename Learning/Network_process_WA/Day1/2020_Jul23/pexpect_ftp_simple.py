import pexpect
ftp = pexpect.spawn("ftp ftp.chandrashekar.info")

ftp.expect("Name.*: ")
ftp.sendline("testuser")

ftp.expect("Password: ", timeout=60)
ftp.sendline("w3lc0me")

ftp.expect("ftp> ")
ftp.sendline("cd /www/files")

ftp.expect("ftp> ")
ftp.sendline("get xml.zip")

ftp.expect("ftp> ")
ftp.sendline("bye")

ftp.close()
