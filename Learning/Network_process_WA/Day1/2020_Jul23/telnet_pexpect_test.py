import pexpect
with open("telnet.log", "ab") as log:
    tn = pexpect.spawn("telnet 192.168.56.101 2023", logfile=log)

    tn.expect("archvm login: ")
    tn.sendline("pythonista")

    tn.expect("Password: ")
    tn.sendline("welcome")

    tn.expect(rb"\[pythonista@archvm ~\]\$ ")
    tn.sendline("uname -a")

    tn.expect(rb"\[pythonista@archvm ~\]\$ ")
    print(tn.before)

    tn.close()
