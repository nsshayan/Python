import pexpect

ftp_commands = [
        ("Name .*: ", "testuser"),
        ("Password .*: ", "w3lcome")
        ("ftp> ", ["cd /www/files/python",
                   "get may27.zip",
                   "quit"])]

def run_commands(program, commands):
    child = pexpect.spawn(program)
    for prompt, command in commands:
        if type(command) is str:
            child.expect(prompt)
            child.sendline(command)
        elif type(command) is list:
            for c in command:
                child.expect(prompt)
                child.sendline(c)


if __name__ == '__main__':
    run_commands("ftp ftp.chandrashekar.info",
                 ftp_commands)
