
commands = [
            ("Name .*: ", "testuser"),
            ("Password: ", "w3lc0me"),
            ("ftp> ", ["cd /www/files/python", "get userdb.py", "quit"])
        ]


def run_command(program, commands):
    import pexpect
    child = pexpect.spawn(program, encoding="utf8")
    for prompt, cmd in commands:
        if type(cmd) is list:
            for c in cmd:
                child.expect(prompt)
                child.sendline(c)
        else:
            child.expect(prompt)
            child.sendline(cmd)
    child.close()


if __name__ == '__main__':
    run_command("ftp ftp.chandrashekar.info", commands)
