import pexpect
with open("log.txt", "w") as log:

    child = pexpect.spawn('telnet 192.168.169.1', 
                           logfile=log)

    child.expect('login: ')
    child.sendline('hame')

    child.expect('Password:', timeout=10)
    child.sendline('hame')

    child.expect("# ")
    child.sendline("ifconfig")

    child.expect("# ")
    output = child.before.splitlines()
    for line in output: 
        if "inet" in line: 
            print(line.split()[1].split(":")[1])

    child.sendline('exit')
    child.close()

