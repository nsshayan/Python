import pexpect



with open("ftp_transcript.log", "wb") as log:
    ftp = pexpect.spawn("ftp ftp.chandrashekar.info", 
                        logfile=log, timeout=5)
    
    ftp.expect("Connected.+220.+Name.+: ")
    ftp.sendline("testuser")
    
    ftp.expect("331.+Password: ")
    ftp.sendline("w3lc0me")

    ftp.expect("230.+ftp> ")       
    ftp.sendline("cd /www/files")
    ftp.expect("250.+ftp> ")
    ftp.sendline("binary")
    
    ftp.expect("200.+ftp> ")
    print(ftp.after, end="", flush=True)
    ftp.interact()
 
    print("Back to program...") 
    ftp.close()
    