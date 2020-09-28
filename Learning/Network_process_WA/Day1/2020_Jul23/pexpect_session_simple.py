def pexpect_session(yaml_file, output):
    import yaml
    import pexpect

    with open(yaml_file) as infile:
        session = yaml.load(infile, Loader=yaml.CLoader)
    
    for command, transcript in session.items():
        with pexpect.spawn(command, encoding="utf8") as p:
            for prompt, reply in transcript:
                p.expect(prompt)
                output.write(p.before)
                p.sendline(reply)
    
if __name__ == '__main__':
    import sys
    pexpect_session("sftp_session.yml", sys.stdout)