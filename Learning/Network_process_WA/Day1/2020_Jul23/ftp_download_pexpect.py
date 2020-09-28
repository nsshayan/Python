import pexpect
with open("ftp_expect_transcript.log", "wb") as logfile:
    ftp = pexpect.spawn("ftp ftp.chandrashekar.info", logfile=logfile)

    ftp.expect(r"Name .+: ")
    ftp.sendline("testuser")

    ftp.expect("Password: ")
    ftp.sendline("w3lc0me")

    ftp.expect("ftp>")
    ftp.sendline("cd /www/files")

    r = ftp.expect(["ftp>", "Error .*", "Connecting", '.+'])
    if r == 0:

    ftp.sendline("binary")

    ftp.expect("ftp>")
    ftp.sendline("get xml.zip")

    ftp.expect("ftp>")
    print(str(ftp.before, "utf8"))
    ftp.sendline("quit")

    ftp.close()
