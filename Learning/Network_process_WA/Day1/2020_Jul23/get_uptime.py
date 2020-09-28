import pexpect

prompt_string = "\[user01@triton ~\]\$"
child = pexpect.spawn("ssh user01@192.168.1.130", encoding="utf8")

child.expect("password: ")
child.sendline("w3lc0me")

child.expect(prompt_string)
child.sendline("uptime")

child.expect(prompt_string)
print(child.before)

child.sendline("exit")
child.close()
