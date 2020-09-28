import pexpect

with open("ftp_session.log", "w") as outfile:
    with pexpect.spawn("ftp ftp.chandrashekar.info",
                        encoding="utf8",
                        logfile=outfile) as ftp:
       # ret = ftp.expect(["Name .+:", "Redirecting .+", "Error .+"])
       # if ret == 0:
       #     # Got "Name:"
       # elif ret == 1:
            # Got Redirecting..."


        ftp.expect("Name .+: ", timeout=10)
        ftp.sendline("testuser")

        ftp.expect("Password: ")
        ftp.sendline("w3lc0me")
        ftp.expect("ftp>")

        ftp.sendline("cd /www/files")
        ftp.expect("ftp>")

        ftp.sendline("ls")
        ftp.expect("ftp>")
        print(ftp.before)

        ftp.sendline("quit")




