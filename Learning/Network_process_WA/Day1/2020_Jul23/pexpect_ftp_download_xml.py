import pexpect

outfile = open("ftp_transcript.log", "w")
ftp = pexpect.spawn("ftp ftp.chandrashekar.info", logfile=outfile, encoding="utf8")

#r = ftp.expect(["aaa", "bbb", "ccc"])
#if r == 0:
#    # expected 'aaa'
#    ftp.sendline("reply_a")
#elif r == 1:
#    # expected 'bbb'
#    ftp.sendline("reply_b")

ftp.expect(r"Name.+: ")
ftp.sendline("testuser")

ftp.expect(r"Password: ")
ftp.sendline("w3lc0me")

ftp.expect(r"test> ", timeout=5)
ftp.sendline("cd /www/files")

ftp.expect(r"ftp> ")
ftp.sendline("bin")

ftp.expect("ftp> ")
ftp.sendline("get xml.zip")

ftp.expect("ftp> ")
print(ftp.before)
ftp.close()
