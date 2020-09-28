
def run_command(program, commands):
    import pexpect

    child = pexpect.spawn(program, encoding="utf8")
    for prompt, command in commands:
        if type(command) is list:
            for c in command:
                child.expect(prompt)
                child.sendline(c)
        else:
            child.expect(prompt)
            child.sendline(command)


if __name__ == '__main__':
    # ftp_session = [
    #    (r"Name.*: ", "testuser"),
    #    (r"Password: ", "w3lc0me"),
    #    (r"ftp> ", ["cd /www/files", "get xml.zip", "quit"])
    # ]

    #run_command("ftp ftp.chandrashekar.info", ftp_session)

    import yaml
    with open("ftp_session.yml") as infile:
        session = yaml.load(infile)
        run_command("ftp ftp.chandrashekar.info", session)
