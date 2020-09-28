def pexpect_session(yaml_file, output):
    import yaml
    import pexpect

    with open(yaml_file) as infile:
        session = yaml.load(infile, Loader=yaml.CLoader) 
    for command, transcript in session.items():
        prompts = list(transcript.keys())        
        with pexpect.spawn(command, encoding="utf8") as p:
            try:
                while True:
                    r = p.expect(prompts)
                    output.write(p.before)
                    reply = transcript[prompts[r]]
                    if type(reply) is str:
                        p.sendline(reply)
                    elif type(reply) is list:
                        for c in reply:
                            p.sendline(c)
                            p.expect(prompts[r])
                            output.write(p.before)
            except pexpect.EOF:
                pass

if __name__ == '__main__':
    import sys
    pexpect_session("sftp_session_better.yml", sys.stdout)