def run_commands(cmd, command_list):
    import pexpect
    outfile = open("runcommands.out", "wb")
    child = pexpect.spawn(cmd, logfile=outfile)
    for prompt, command in command_list:
        if type(command) is list:
            for c in command:
                child.expect(prompt)
                child.sendline(c)
        else:
            child.expect(prompt)
            child.sendline(command)
    outfile.close()


if __name__ == '__main__':
    commands = [
        ("Name .*: ", "testuser"),
        ("Password: ", "w3lc0me"),
        ("ftp>", ["cd /www/files/python", "ls", "get may27.zip", "quit"])
    ]

    run_commands("ftp ftp.chandrashekar.info", commands)
    
# https://public.etherpad-mozilla.org/p/Advanced_Python



