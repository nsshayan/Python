commands = [
    {"program": "ftp ftp.chandrashekar.info",
     "commands": [
         ("Name .*: ", "testuser"),
         ("Password: ", "w3lc0me"),
         ("ftp> ", ["cd /www/files", "get test.txt", "quit"])
     ]
     },
]


def run_commands(c, logfile=None):
    import pexpect
    log = open(logfile, "a") if logfile else None

    if type(c) is str:
        import yaml
        with open(c) as infile:
            c = yaml.load(infile)

    for rec in c:
        child = pexpect.spawn(rec["program"], logfile=log)

        for prompt, command in rec["commands"]:
            if type(command) is str:
                child.expect(prompt)
                child.sendline(command)
            elif type(command) is list:
                for cmd in command:
                    child.expect(prompt)
                    child.sendline(cmd)


if __name__ == '__main__':
    # run_commands(commands)
    run_commands("ftp_commands.yml")
