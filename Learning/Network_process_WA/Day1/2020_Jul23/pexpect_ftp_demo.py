import pexpect

with open("ftpsession.log", "wb") as log:
    ftp = pexpect.spawn("ftp ftp.chandrashekar.info", 
                        logfile=log, timeout=5)

    ftp.expect(r"Name.+: ", timeout=10)
    print(ftp.before)

    ftp.sendline("testuser")
    ftp.expect(r"Password: ")
    print(ftp.before)

    ftp.sendline("w3lc0me")
    ftp.expect("ftp> ")
    print(ftp.before)

    ftp.sendline("cd /www/files")
    ftp.expect("ftp> ")
    print(ftp.before)

    ftp.sendline("get xml23423.zip")
    ftp.expect("ftp>", timeout=15)
    print(ftp.before)

    ftp.sendline("quit")

    ftp.close()

