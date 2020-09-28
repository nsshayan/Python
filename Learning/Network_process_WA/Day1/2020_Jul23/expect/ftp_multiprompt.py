import pexpect

outfile = open("ftp_session.log", "wb")
child = pexpect.spawn("ftp ftp.chandrashekar.info", logfile=outfile)

child.expect("Name .*: ", timeout=10)
child.sendline("testuser")

child.expect("Password: ", timeout=10)
child.sendline("w3lc0me")

child.expect("ftp>", timeout=10)
child.sendline("cd /www/files/python")

child.expect("ftp>", timeout=10)
child.sendline("get may27.zip")

child.expect("ftp>", timeout=30)
child.sendline("quit")
child.close()
outfile.close()


