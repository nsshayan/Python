commands = [
        {"program": "ftp ftp.chandrashekar.info",
         "commands": [
                     ("Name .*: ", "testuser"),
                     ("Password: ", "w3lc0me"),
                     ("ftp> ", ["cd /www/files", "get test.txt", "quit"])
                 ]
        },

]

def run_commands(c):
    import pexpect
    for rec in c:
        child = pexpect.spawn(rec["program"])
        for prompt, command in rec["commands"]:
            if type(command) is str:
                child.expect(prompt)
                child.sendline(command)
            elif type(command) is list:
                for cmd in command:
                    child.expect(prompt)
                    child.sendline(cmd)
        child.close()


if __name__ == '__main__':
    run_commands(commands)
