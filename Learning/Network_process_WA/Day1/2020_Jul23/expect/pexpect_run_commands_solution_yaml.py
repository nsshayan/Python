
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
    import yaml
    with open("ftp_session.yml") as commands_file:
        commands = yaml.load(commands_file)
    run_commands(commands)
