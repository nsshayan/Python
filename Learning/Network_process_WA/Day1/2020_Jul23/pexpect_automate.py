
def pexpect_run_command(command, transcript):
    import pexpect
    proc = pexpect.spawn(command)
    for prompt, reply in transcript:
        if type(reply) is str:
            proc.expect(prompt)
            proc.sendline(reply)
        elif type(reply) is list:
            for r in reply:
                proc.expect(prompt)
                proc.sendline(r)
    proc.close()


if __name__ == '__main__':
    #download_xml_file = [
    #    ("Name.+: ", "testuser"),
    #    ("Password: ", "w3lc0me"),
    #    ("ftp> ", ["cd /www/files", "binary", "get xml.zip", "quit"])
    #]

    import yaml
    with open("download_xml.yml") as infile:
        pexpect_run_command(
            "ftp ftp.chandrashekar.info",
            yaml.load(infile))


