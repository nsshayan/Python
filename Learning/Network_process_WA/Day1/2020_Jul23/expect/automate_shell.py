from pexpect import spawn

outfile = open("shellout.log", "wb")

shell = spawn("bash", logfile=outfile)

shell.expect('ganymede:.*\$ ', timeout=3)
shell.sendline("pwd")
print("pwd = ", shell.before)

shell.expect('ganymede:.*\$')
shell.sendline("ftp ftp.chandrashekar.info")

shell.expect("Name.*:")
shell.sendline("testuser")
print(shell.before)

shell.expect("Password:")
shell.sendline("w3lc0me")

shell.expect("ftp>")
shell.sendline("ls")

shell.expect("ftp>")
print(shell.before)

shell.close()


