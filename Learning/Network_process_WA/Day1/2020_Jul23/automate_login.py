import pexpect
with open("ftp_transcript.log", "wb") as logfile:
    ftp = pexpect.spawn("ftp ftp.chandrashekar.info", logfile=logfile)

    ftp.expect(r"Name.*: ")
    ftp.sendline("testuser")

    ftp.expect(r"Password: ")
    ftp.sendline("w3lc0me")

    ftp.expect("ftp> ")
    print(ftp.after, end="", flush=True)

    ftp.interact()
    print("Back to program...")
    ftp.close()
