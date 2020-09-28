import pexpect

tc = pexpect.spawn("telnet 192.168.56.104 2023")

tc.expect("login: ")

tc.sendline("pythonista")
tc.expect("Password: ")

tc.sendline("welcome")
tc.expect_exact("[pythonista@archvm ~]$ ")

tc.sendline("uname -a")
tc.expect_exact("[pythonista@archvm ~]$ ")
print(tc.before)

tc.close()


