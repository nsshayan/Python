#ftp_commands = [
#    ("Name .+: ", "testuser"),
#    ("Password:", "w3lc0me"),
#    ("ftp> ", ["binary", "passive", "cd /www/files", "get dec19.zip", "quit"])
#]

def run_script(program, commands):
    import pexpect
    import sys
    child = pexpect.spawn(program, logfile=sys.stdout, encoding="utf8")

    for e, s in commands:
        if type(s) is list:
            for c in s:
                child.expect(e)
                child.sendline(c)
        else:
            child.expect(e)
            child.sendline(s)



if __name__ == '__main__':
    import yaml
    with open("ftp_commands.yml") as infile:
        ftp_commands = yaml.load(infile)

    run_script("ftp ftp.chandrashekar.info", ftp_commands)

