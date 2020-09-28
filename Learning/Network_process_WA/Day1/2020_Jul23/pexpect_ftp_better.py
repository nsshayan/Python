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
    for command in commands:
        child = pexpect.spawn(command, logfile=logfile)
        for prompt, reply in commands[command]:
            if isinstance(reply, (list, tuple)):
                for r in reply:
                    child.expect(prompt)
                    child.sendline(r)
            else:
                child.expect(prompt)
                child.sendline(reply)


if __name__ == '__main__':
    with open("ftp_transcript.log", "wb") as outfile:
        expect_transcript(commands, logfile=outfile)
