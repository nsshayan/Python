import pexpect


def parse_input(s):
    return s.lower()


def parse_output(s):
    return s.upper()


with open("ftp_transcript.log", "wb") as logfile:
    ftp = pexpect.spawn("ftp ftp.chandrashekar.info", logfile=logfile)

    ftp.expect(r"Name.*: ")
    ftp.sendline("testuser")

    ftp.expect(r"Password: ")
    ftp.sendline("w3lc0me")

    ftp.expect("ftp> ")
    print("ftp> ", end="")

    ftp.interact(input_filter=parse_input, output_filter=parse_output)
    print("Back to program...")
    ftp.close()
