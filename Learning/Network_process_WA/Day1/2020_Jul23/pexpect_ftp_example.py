import pexpect

ftp_log = open("pexpect_ftp.log", "w")
ftp = pexpect.spawn("ftp ftp.chandrashekar.info",
                    encoding="utf8", logfile=ftp_log, timeout=5)

ftp.expect(r"Name.*: ")

ftp.sendline("testuser")
ftp.expect("Password:")

ftp.sendline("w3lc0me")
ftp.expect("230.+ftp> ")

ftp.sendline("cd /www/files")
r = ftp.expect(["550.+ftp>", "250.+ftp>"])
if r == 0:
    print("Failed to change directory...")

elif r == 1:
    ftp.sendline("get xml.zip")
    ftp.expect("226.+ftp>", timeout=5000)
    print(ftp.before)

ftp.sendline("quit")

ftp.close()
ftp_log.close()
