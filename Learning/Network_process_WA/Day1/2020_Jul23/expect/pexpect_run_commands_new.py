import pexpect

download_commands = ["cd /www/files\r", "get test.txt\r", "quit\r"]

def testfn(*args):
    print("---", args)
    return download_commands.pop(0)

# Tuple-set
ftp_session = [
    ("Name .*:", "testuser\r"),
    ("Password: ", "w3lc0me\r"),
    ("ftp> ", testfn),
]

with open("ftp.log", "wb") as ftp_log:
    pexpect.run("ftp ftp.chandrashekar.info", events=ftp_session, logfile=ftp_log)
