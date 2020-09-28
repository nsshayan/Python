import pexpect
child = pexpect.spawn('ftp ftp.chandrashekar.info',
                      logfile=open("log.txt", "wb"))

child.expect('Name .*: ')
child.sendline('testuser')

child.expect('Password:')
child.sendline('w3lc0me')


child.expect('ftp> ')
child.sendline("cd /www/files")

child.expect("ftp> ")
child.sendline("")

print("Logged in to FTP...")
child.interact()

print("Back to my program...")
