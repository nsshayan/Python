import pexpect
from getpass import getpass




with open("ftp.log", "w") as outfile:
    ftp = pexpect.spawn("ftp ftp.chandrashekar.info",
                        encoding="utf8", logfile=outfile)

    ftp.expect("Name.+: ")
    print(ftp.before)
    username = input(ftp.after)
    ftp.sendline(username)

    while True:
        ftp.expect("Password: ")
        print(ftp.before)
        password = getpass(ftp.after)
        ftp.sendline(password)

        r = ftp.expect(["230.+ftp> ", "530.+ftp> ", pexpect.TIMEOUT], timeout=5)
        if r == 0:
            break
        print(ftp.before)
        print(">>> Incorrect password.")
        ftp.sendline(f"user {username}")

    ftp.sendline("cd /files")

    ftp.expect("250.+ftp> ")
    ftp.before
    ftp.sendline("binary")

    ftp.expect("ftp>")
    ftp.sendline("get xml.zip")

    ftp.expect("ftp>")
    print(ftp.before)
    ftp.sendline("bye")
    ftp.close()
