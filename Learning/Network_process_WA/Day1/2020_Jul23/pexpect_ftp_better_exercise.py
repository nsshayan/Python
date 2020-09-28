commands = {
    "ftp ftp.chandrashekar.info": [
        ("Name .*:", "testuser"),
        ("Password: ", "w3lc0me"),
        ("ftp> ", ["cd /www/files",
                   "get xml.zip",
                   "quit"])
    ]
}


def expect_transcript(commands, logfile=None):
    import pexpect
    for command, session in commands.items():
        with pexpect.spawn(command,
                           encoding="utf8",
                           logfile=logfile) as proc:

            for prompt, reply in session:
                proc.expect(prompt)
                if isinstance(reply, str):
                    proc.sendline(reply)
                elif isinstance(reply, list):
                    for c in reply:
                        proc.sendline(c)
                        try:
                            proc.expect(prompt)
                        except pexpect.EOF:
                            break


if __name__ == '__main__':
    with open("ftp_transcript.log", "w") as outfile:
        expect_transcript(commands, logfile=outfile)
