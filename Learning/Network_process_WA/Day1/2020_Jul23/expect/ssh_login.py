import pexpect
with open("output.log", "w") as log:
    child = pexpect.spawn("ssh joe@192.168.169.5", logfile=log)

    child.expect("ssword: ")
    child.sendline("w3lc0me")

    child.expect(r"$")
    child.sendline("uname -a")
    
    child.expect(r"$")
    print(child.before)

