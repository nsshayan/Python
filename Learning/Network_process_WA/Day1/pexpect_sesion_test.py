prompt_string = "\[user01@triton ~\]\$"
ssh_session = {
    "command": "ssh user01@192.168.1.130",
    "session": [
        ("password:" "w3lc0me"),
        (prompt_string, ["uptime", "uname -a", "who", "exit"])
    ]
}
def pexpect_session(session):
    pass # TODO
if __name__ == '__main__':
    pexpect_session(ssh_session)
