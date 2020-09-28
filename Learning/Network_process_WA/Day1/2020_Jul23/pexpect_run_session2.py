def expect_transcript_old(commands, logfile=None):
    import pexpect
    for program, transcript in commands.items():
        proc = pexpect.spawn(program)
        for prompt, reply in transcript:
            if type(reply) is str:
                proc.expect(prompt)
                yield proc.before
                proc.sendline(reply)
            elif type(reply) is list:
                for r in reply:
                    proc.expect(prompt)
                    yield proc.before
                    proc.sendline(r)

def expect_transcript(commands, logfile=None):
    import pexpect
    for program, transcript in command.items():
        proc = pexpect.run(program, events=transcript)

if __name__ == '__main__':
    import sys
    import yaml

    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} yaml-file")
        exit(1)

    with open(sys.argv[1]) as yaml_file:
        commands = yaml.load(yaml_file, Loader=yaml.CLoader)

    with open("ftp_transcript.log", "w") as outfile:
        for output in expect_transcript(commands, logfile=outfile):
            print(output)
            print("-" * 40)
