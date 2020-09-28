import pexpect
import sys

try:
    #with open("ftp_transcript.log", "wb") as outfile:
    child = pexpect.spawn("ftp ftp.chandrashekar.info", encoding="utf8")
                          #logfile=sys.stdout, encoding="utf8")

    r = child.expect(["Test .+: ", "Name .+: ", "Username .+: "], timeout=2)
    print("Got ", r)
    child.sendline("testuser")

    child.expect("Password:")
    child.sendline("w3lc0me")

    child.expect("ftp> ")
    child.sendline("binary")

    child.expect("ftp> ")
    child.sendline("passive")

    child.expect("ftp> ")
    child.sendline("cd /www/files")

    child.expect("ftp> ")
    #child.sendline("get dec19.zip")

    child.sendline("dir")
    child.expect("ftp> ")
    print(child.before)
    child.close()
except Exception as e:
    import pdb
    pdb.set_trace()
