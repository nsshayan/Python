import pexpect

with pexpect.spawn("ftp ftp.chandrashekar.info") as ftp:
    ftp.expect("Name.+:")
    ftp.sendline("testuser")
    
    ftp.expect("Password:")
    ftp.sendline("w3lc0me")
    
    ftp.expect("ftp>")
    ftp.sendline("cd /www/files")
    
    ftp.expect("ftp>")
    ftp.sendline("get xml.zip")
    
    ftp.expect("ftp>")
    print(ftp.before)

    ftp.sendline("quit")
    
    