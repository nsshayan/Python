
def ftp_session(command, ftp_config):
    import pexpect
    proc = pexpect.spawn(command)
    for prompt, reply in ftp_config:
        if isinstance(reply, list):
            for c in reply:
                proc.expect(prompt, timeout=5)
                proc.sendline(c)
        elif isinstance(reply, str):
            proc.expect(prompt)
            proc.sendline(reply)




if __name__ == '__main__':
    download_xml_file = [
        ("Name .+: ", "testuser"),
        ("Password: ", "w3lc0me"),
        ("ftp> ", ["cd /www/files", "bin", "get xml.zip", "quit"])
    ]

    ftp_session("ftp ftp.chandrashekar.info", download_xml_file)
