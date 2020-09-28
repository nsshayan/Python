import pexpect
from getpass import getpass

with pexpect.spawn("ftp ftp.chandrashekar.info", timeout=20) as ftp:
    ftp.expect("Name (.+):")
    ftp.sendline("testuser")

    while True:
        ftp.expect("Password:")
        password = getpass("Enter password: ")
        ftp.sendline(password)

        r = ftp.expect([r"230 User logged in.+ftp>", r"530 Login incorrect.+ftp>"])
        if r == 0:
            break
        elif r == 1:
            print("Incorrect password.")
            ftp.sendline("user testuser")

    ftp.sendline("cd /www/files")

    ftp.expect("ftp>")
    ftp.sendline("get xml.zip")

    ftp.expect("ftp>", timeout=30)
    ftp.sendline("quit")
