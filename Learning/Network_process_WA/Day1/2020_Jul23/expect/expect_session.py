def expect_session(command, session, *args, **kwargs):
    import yaml
    from pexpect import spawn
    child = spawn(command, *args, **kwargs)

    if type(session) is str:
        with open(session) as infile:
            session = yaml.load(infile)

    for rec in session:
        if "send" in rec:
            child.expect(bytes(rec["expect"], "utf8"), 
                         timeout=rec.get("timeout", None))
            if "get_output" in rec:
                print(str(child.before, "utf8"))
            child.sendline(bytes(rec["send"], "utf8"))
        elif "send_commands" in rec:
            for cmd in bytes(rec["send_commands"], "utf8"):
                child.expect(bytes(rec["expect"], "utf8"), 
                                   timeout=rec.get("timeout", None))
                child.sendline(cmd)
        else:
            raise TypeError("Invalid format for command")
    child.close()


if __name__ == '__main__':

    with open("telnet_session.log", "wb") as outfile:
        expect_session("telnet -l pythonista 192.168.56.101",
                       "telnet_session.yml",
                       logfile=outfile)


