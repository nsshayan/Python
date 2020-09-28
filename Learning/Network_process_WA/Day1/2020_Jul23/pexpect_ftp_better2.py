

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
    import yaml
    with open("ftp_session.yml") as infile:
        commands = yaml.load(infile)

    print(commands)
    with open("ftp_transcript.log", "wb") as outfile:
        expect_transcript(commands, logfile=outfile)
