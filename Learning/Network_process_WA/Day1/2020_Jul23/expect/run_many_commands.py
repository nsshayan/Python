import pexpect
import logging

ftp_commands = [
        ("Name .*: ", "testuser"),
        ("Password .*: ", "w3lc0me"),
        ("ftp> ", ["cd /www/files/python",
                   "get may27.zip",
                   "quit"])]

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

def run_commands_old(program, commands):
    ftplog = open("ftplog.log", "wb")
    child = pexpect.spawn(program, logfile=ftplog)

    for prompt, command in commands:
        if type(command) is str:
            child.expect(prompt)
            child.sendline(command)
        elif type(command) is list:
            for c in command:
                child.expect(prompt)
                child.sendline(c)
    child.close()
    ftplog.close()

if __name__ == '__main__':
    #logging.basicConfig(filename="run_commands.log")

    #with open("ftpsession.log", "wb") as ftp_log:
    run_commands_old("ftp ftp.chandrashekar.info",
                 ftp_commands)
