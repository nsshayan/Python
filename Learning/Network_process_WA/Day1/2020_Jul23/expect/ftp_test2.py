from pexpect import spawn

ftp = spawn("ftp ftp.chandrashekar.info")

ftp.expect("Name .*: ")
ftp.sendline("testuser")
print("Sent username: ", ftp.before)

ftp.expect("Password: ")
ftp.sendline("w3lc0me")
#print("Sent password: ", ftp.before)

ftp.expect("ftp> ")
ftp.sendline("cd /www/files/python")
print("Sent cd command: ", ftp.before)
print("Sent cd command: ", ftp.before)

ftp.expect("ftp> ")
ftp.sendline("put test.dat")

ftp.close()

