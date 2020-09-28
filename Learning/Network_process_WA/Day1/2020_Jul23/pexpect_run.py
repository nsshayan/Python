
def pexpect_run(config):
    import pexpect

    command = pexpect.spawn(config["program"], encoding="utf8")
    for prompt, reply in config["commands"]:
        if isinstance(reply, list):
            for c in reply:
                command.expect(prompt)
                command.sendline(c)
        else:
            command.expect(prompt)
            command.sendline(reply)

if __name__ == '__main__':
    import yaml
    with open("ftp_commands.yml") as infile:
        ftp_config = yaml.load(infile)
    pexpect_run(ftp_config)
