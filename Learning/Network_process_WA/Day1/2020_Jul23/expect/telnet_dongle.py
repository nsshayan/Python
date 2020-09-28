import pexpect
with open("log.txt", "w") as log:

    child = pexpect.spawn('telnet 192.168.169.1', 
                           logfile=log)

    child.expect('login: ')
    child.sendline('hame')

    child.expect('Password:', timeout=10)
    child.sendline('hame')

    child.expect('# ')
    child.sendline('ls /')
    child.expect('# ')

    print(child.before)

    child.sendline("cat /proc/cpuinfo")

    child.expect("# ")
    print("-" * 40)
    output = child.before
    print(output.upper())

    child.sendline('exit')
    child.close()

