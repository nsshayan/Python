import pexpect
from getpass import getpass

ftp = pexpect.spawn("ftp ftp.chandrashekar.info", encoding="utf8")

ftp.expect("Name.+:")
ftp.sendline("testuser")

ftp.expect("Password:")
password = getpass("Enter password: ")
ftp.sendline(password)

password_success = ["230.+ftp>", "530.+ftp>"]

r = ftp.expect(password_success)
if r == 1:
    print("Password is incorrect.")
    exit(1)

ftp.sendline("cd /www/files")

ftp.expect("ftp>")
ftp.sendline("bin")

ftp.expect("ftp>")
ftp.sendline("get xml.zip")

ftp.expect("ftp>")
ftp.sendline("quit")

ftp.close()
