def run_command(command, transcript):
    import pexpect

    child = pexpect.spawn(command)
    for prompt, reply in transcript:
        child.expect(prompt)
        if isinstance(reply, list):
            for r in reply:
                child.sendline(r)
                try:
                    child.expect(prompt)
                except pexpect.EOF:
                    break
        else:
            child.sendline(reply)


if __name__ == '__main__':
    ftp_transcript = [
        (r"Name.*: ", "testuser"),
        (r"Password: ", "w3lc0me"),
        (r"ftp> ", ["cd /www/files", "get xml.zip", "quit"])
    ]

    run_command("ftp ftp.chandrashekar.info", ftp_transcript)


