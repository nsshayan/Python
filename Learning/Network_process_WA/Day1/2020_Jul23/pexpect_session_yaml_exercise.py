
def pexpect_session(yaml_file, output):
    import yaml
    import pexpect
    with open(yaml_file) as infile:
        config = yaml.load(infile, Loader=yaml.CLoader)

        with open("pexpect.log", "w") as command_log, \
             pexpect.spawn(
                 config["command"],
                 encoding="utf8",
                 logfile=command_log) as proc:
            try:
                for prompt, reply in config["session"].items():
                    proc.expect(prompt)
                    print(proc.before, file=output)
                    if isinstance(reply, list):
                        for cmd in reply:
                            proc.sendline(cmd)
                            proc.expect(prompt)
                            print(proc.before, file=output)
                    else:
                        proc.sendline(reply)
            except pexpect.EOF:
                print("Program exited.")

if __name__ == '__main__':
    import sys
    pexpect_session("telnet_session.yml", sys.stdout)
