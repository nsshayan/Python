prompt_string = "\[user01@triton ~\]\$"
ssh_session = {
    "command": "ssh user01@192.168.1.130",
    "session": [
        ("password:", "w3lc0me"),
        (prompt_string, ["uptime", "uname -a", "who", "exit"])
    ]
}


def pexpect_session(session):
    import pexpect
    with pexpect.spawn(session["command"], encoding="utf8") as proc:
        for prompt, reply in session["session"]:
            if isinstance(reply, str):
                proc.expect(prompt)
                proc.sendline(reply)
            else:
                for r in reply:
                    proc.expect(prompt)
                    print(proc.before)
                    proc.sendline(r)


if __name__ == '__main__':
    pexpect_session(ssh_session)
