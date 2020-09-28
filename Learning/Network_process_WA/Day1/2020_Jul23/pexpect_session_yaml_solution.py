
def pexpect_session(yaml_file, output):
    import yaml
    import pexpect
    with open(yaml_file) as infile:
        transcript = yaml.load(infile)

    session = pexpect.spawn(transcript["command"], encoding="utf8")
    for prompt, reply in transcript["session"]:
        if type(reply) is list:
            for r in reply:
                if session.before: output.write(session.before)
                session.expect(prompt)
                session.sendline(r)
        elif type(reply) is str:
            if session.before: output.write(session.before)
            session.expect(prompt)
            session.sendline(reply)


if __name__ == '__main__':
    import sys
    pexpect_session("telnet_session2.yml", sys.stdout)
