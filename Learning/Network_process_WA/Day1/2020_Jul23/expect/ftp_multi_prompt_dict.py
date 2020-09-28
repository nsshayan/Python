import pexpect
child = pexpect.spawn('ftp ftp.chandrashekar.info', 
                       logfile=open("log.txt", "w"))
# r = child.expect(['Name .*: ', 'Error .*', 'Redirecting .*'])
# if r == 0:
    # got name
#    pass
#  elif r == 1:

child.expect('Name .*: ')
child.sendline('testuser')

child.expect('Password:')
child.sendline('w3lc0me')

child.expect('ftp> ')
child.sendline('cd /www/files/python')

child.expect('ftp> ', timeout=20)
child.sendline('get users.txt')

child.expect('ftp> ')
child.sendline("quit")

#child.interact()

