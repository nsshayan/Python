import pexpect

def process_input(a):
    print("Input processing - ", a)
    return a.lower()

def process_output(a):
    print("Output processing - ", a)
    return a.upper()

log = open("ftp_pexpect.log", "ab")

ftp = pexpect.spawn("ftp ftp.chandrashekar.info", logfile=log)
ftp.expect(b"Name .*: ")
ftp.sendline(b"testuser")

ftp.expect(b"Password: ")
ftp.sendline(b"w3lc0me")

ftp.expect(b"ftp> ")
ftp.sendline(b"")
ftp.interact(input_filter=process_input, output_filter=process_output)
print("Back to program..")
#ftp.sendline("cd /www/files/python")

#ftp.expect("ftp> ")
#ftp.sendline("get userdb.py")

#ftp.expect("ftp> ")
#ftp.sendline("quit")

ftp.close()

