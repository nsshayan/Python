
def run_command(yaml_file):
    import yaml
    with open(yaml_file) as infile:
        config = yaml.load(infile, Loader=yaml.CLoader)

    import pexpect
    for program, session in config.items():
        process = pexpect.spawn(program)

        for prompt, reply in session:
            if isinstance(reply, list):
                for r in reply:
                    process.expect(prompt)
                    process.sendline(r)
            else:
                process.expect(prompt)
                process.sendline(reply)

if __name__ == '__main__':
   run_command("ftp_session.yml")
   