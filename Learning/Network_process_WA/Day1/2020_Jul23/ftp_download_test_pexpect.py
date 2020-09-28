import pexpect
ftp_log = open("ftp.log", "ab")

ftp = pexpect.spawn("ftp ftp.chandrashekar.info",
                    logfile=ftp_log)

r = ftp.expect(b"Name .+: ")
ftp.sendline(b"testuser")

ftp.expect(b"Password: ")
ftp.sendline(b"w3lc0me")

ftp.expect(b"ftp>")
ftp.sendline(b"cd /www/files")


def output_handler(s):
    return s.upper()


def input_handler(s):
    return s.lower()


ftp.interact(input_filter=input_handler, output_filter=output_handler)

print("Back to program...")

ftp.sendline("quit")

# ftp.expect("ftp>")
#ftp.sendline("get xml.zip")

# ftp.expect("ftp>")
# print(ftp.before)
# ftp.sendline("quit")

ftp.close()
