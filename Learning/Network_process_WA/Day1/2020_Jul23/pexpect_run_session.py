
def expect_transcript(commands, logfile=None):
    import pexpect
    for command, session in commands.items():
        with pexpect.spawn(command,
                           encoding="utf8",
                           logfile=logfile) as proc:

            for prompt, reply in session:
                proc.expect(prompt)
                yield proc.before
                if isinstance(reply, str):
                    proc.sendline(reply)
                elif isinstance(reply, list):
                    for c in reply:
                        proc.sendline(c)
                        try:
                            proc.expect(prompt)
                            yield proc.before
                        except pexpect.EOF:
                            break


if __name__ == '__main__':
    import sys
    import yaml

    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} yaml-file")
        exit(1)

    with open(sys.argv[1]) as yaml_file:
        commands = yaml.load(yaml_file)

    with open("ftp_transcript.log", "w") as outfile:
        for output in expect_transcript(commands, logfile=outfile):
            print(output)
            print("-" * 40)
