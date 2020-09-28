import pexpect

with open("ftp_transcript.out", "ab") as outfile:
    ftp = pexpect.spawn("ftp ftp.chandrashekasdfsdfr.info", logfile=outfile)

    ftp.expect(r"Name .*: ")
    ftp.sendline("testuser")

    ftp.expect("Passwrd: ", timeout=5)
    ftp.sendline("w3lc0me")

    ftp.expect("ftp> ")
    ftp.sendline("ls")

    ftp.expect("ftp> ")
    print(str(ftp.before, "utf8"))
    ftp.sendline("quit")

    ftp.close()
