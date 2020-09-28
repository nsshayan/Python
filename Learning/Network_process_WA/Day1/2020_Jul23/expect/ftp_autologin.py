import pexpect
child = pexpect.spawn('ftp ftp.chandrashekar.info',
                      logfile=open("log.txt", "wb"))

child.expect('Name .*: ')
child.sendline('testuser')

child.expect('Password:')
child.sendline('w3lc0me')


child.expect('ftp> ')
child.sendline("")


def send_input(s):
    print("Sending", s)
    return s.lower()


def send_output(s):
    print("Got", s)
    return s.upper()


print("Logged in to FTP...")
#child.interact(input_filter=send_input,
#               output_filter=send_output)
child.interact()

print("Back to my program...")
