def expect_session_old(command, session):
    from pexpect import spawn
    child = spawn(command)

    for expected, cmd in session:
        if type(cmd) is str:
            child.expect(expected)
            child.sendline(cmd)
        elif type(cmd) is list:
            for c in cmd:
                child.expect(expected)
                child.sendline(c)
        else:
            raise TypeError("Invalid format for command")
    child.close()

def expect_session(command, session):
    import yaml
    from pexpect import spawn
    child = spawn(command)

    if type(session) is str:
        with open(session) as infile:
            session = yaml.load(infile)

    for rec in session:
        if "send" in rec:
            child.expect(rec["expect"], timeout=rec.get("timeout", None))
            child.sendline(rec["send"])
        elif "send_commands" in rec:
            for cmd in rec["send_commands"]:
                child.expect(rec["expect"], timeout=rec.get("timeout", None))
                child.sendline(cmd)
        else:
            raise TypeError("Invalid format for command")
    child.close()


if __name__ == '__main__':

    old_ftp_session = [
        ("Name .*: ", "testuser"),
        ("Password: ", "w3lc0me"),
        ("ftp>",  ["cd /www/files/python", "get may27.zip", "quit"])
    ]

    old_ftp_session2 = [
        dict(expect="Name .*: ", send="testuser", timeout=10),
        {"expect": "Password: ", "send": "w3lc0me"},
        dict(expect="ftp> ", send_commands=["cd /www/files/python", "get may27.zip", "quit"])
    ]

    expect_session("ftp ftp.chandrashekar.info", "ftp_session.cmd")


