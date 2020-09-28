from pexpect import spawn

with open("ftp_session.log", "wb") as outfile:
    ftp = spawn("ftp ftp.chandrashekar.info", logfile=outfile)

    ftp.expect(r"Name .+:")
    ftp.sendline("testuser")

    ftp.expect(r"Password: ")
    ftp.sendline("w3lc0me")

    ftp.expect("ftp> ")
    ftp.sendline("cd /www/files")

    ftp.expect("ftp> ")
    ftp.sendline("bin")

    ftp.expect("ftp> ")
    ftp.sendline("get xml.zip")

    ftp.expect("ftp> ")
    ftp.sendline("quit")
    ftp.close()

