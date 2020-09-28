import pexpect

password = input("Enter password: ")

with open("ftp_transcript.log", "w") as log:
    ftp = pexpect.spawn("ftp ftp.chandrashekar.info", 
                        logfile=log, encoding="utf8", timeout=5)
    
    ftp.expect("Connected.+220.+Name.+: ")
    ftp.sendline("testuser")
    
    ftp.expect("331.+Password: ")
    ftp.sendline(password)

    while True:
        r = ftp.expect(["230.+ftp> ", "530.+failed.+ftp> "])
        if r == 1:
            password = input("Password incorrect.\nEnter correct password: ")
            ftp.sendline("user testuser")
            ftp.expect("Password: ")
            ftp.sendline(password)
        else:
            break
        
    ftp.sendline("cd /www/files")
    
    ftp.expect("250.+ftp> ")
    ftp.sendline("binary")
    
    ftp.expect("200.+ftp> ")
    ftp.sendline("get nov26.zip")
    
    ftp.expect("200.+226.+ftp> ", timeout=30)
    ftp.close()
    