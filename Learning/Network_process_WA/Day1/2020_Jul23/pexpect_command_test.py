import pexpect
prompt_string = "\(base\) bash-4\.4\$"

with open("ls_output.log", "w") as logfile:
    shell = pexpect.spawn("bash",
                          encoding="utf8", logfile=logfile)

    shell.expect(prompt_string)
    shell.sendline("ls -lR /opt/zeppelin/")

    shell.expect(prompt_string)
    print(shell.before)

    shell.close()
