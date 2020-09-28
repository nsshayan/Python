# IPython log file

get_ipython().run_line_magic('load', 'http://tinyurl.com/dsize.py')
get_ipython().run_line_magic('load', 'http://tinyurl.com/dsize.py')
get_ipython().run_line_magic('load', 'http://tinyurl.com/dsize-py')
get_ipython().run_line_magic('log', '')
get_ipython().run_line_magic('pinfo', '%logstart')
get_ipython().run_line_magic('logstart', '')
get_ipython().run_line_magic('load', 'http://tinyurl.com/dsize-py')
# %load http://tinyurl.com/dsize-py
"""
Preliminary exercise:
=====================
Calculate and print the total size of all files
in a directory structure, by recursively traversing
and summing up the sizes of each file in the directory.

Example usage:
    $ python3 dirsize.py .
    556289 bytes

    $ python3 dirsize.py /usr/share
    581829804 bytes

"""

def calc_size(start_path):
    pass # TODO: Implement the logic here! 
         # Hint: lookup os.path and os.walk functions

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description=__doc__)
    parser.add_argument("path",
                      help="Path to source directory")

    args = parser.parse_args()

    print(calc_size(args.path), "bytes")

    
import os
os.walk(".")
for r in os.walk("."):
    print(r)
    
for r in os.walk("."):
    print(r)
    input()
    
os.listdir(".")
os.path.getsize("calc_communicate.py")
[ os.path.getsize(f) for f in os.listdir(".") ]
sum([ os.path.getsize(f) for f in os.listdir(".") ])
for path, dirs, files in os.walk("."):
    for f in files:
        print(f)
        
for path, dirs, files in os.walk("."):
    for f in files:
        print(f, os.path.getsize(f))
        
        
d = "./paramiko"
f = "a.txt"
os.path.join(d, f)
d + "/" + f
d = "./paramiko/"
os.path.join(d, f)
d + "/" + f
for path, dirs, files in os.walk("."):
    for f in files:
        filepath = os.path.join(path, f)
        
        print(filepath, os.path.getsize(filepath))
        
from pathlib import Path
p = Path(".")
p
p.absolute()
p.name
p1 = Path("./paramiko")
p1.name
p1 = Path("/usr/bin/ls")
p1.name
p1.cwd
p1.cwd()
p1.joinpath("dsfsdf")
p
p.glob("*")
list(p.glob("*"))
list(p.glob("**/*"))
list(p.glob("**/*"))
p.stat()
p.stat().st_size
p.glob("**/*")
[ f.stat().st_size for f in p.glob("**/*") ]
sum(f.stat().st_size for f in p.glob("**/*"))
c = """mkdir "Program Files" 'Documents and Settings'"""
print(c)
c.split()
from shlex import split
split(c)
import yaml
yaml.load("cmdlist.yml")
yaml.load(open("cmdlist.yml"))
yaml.load(open("cmdlist.yml"))
c = yaml.load(open("cmdlist.yml"))
c["ipaddr"]["ipv4-pattern"]
print(c["ipaddr"]["ipv4-pattern"])
import re
p = re.compile("\d+")
p
type(p)
p.search("sdlkf lsdkfjldsf 234234 s sdkf 234234 sdkfsdkf 23423432")
m = p.search("sdlkf lsdkfjldsf 234234 s sdkf 234234 sdkfsdkf 23423432")
m.start()
m.end()
m.group()
m.string
m.re
p.findall("sdlkf lsdkfjldsf 234234 s sdkf 234234 sdkfsdkf 23423432")
p.finditer("sdlkf lsdkfjldsf 234234 s sdkf 234234 sdkfsdkf 23423432")
list(p.finditer("sdlkf lsdkfjldsf 234234 s sdkf 234234 sdkfsdkf 23423432"))
import yaml
with open("cmdlist.yml") as yaml_file: config = yaml.load(yaml_file)
config
import os
os.environ
os.environ.keys()
os.environ["PATH"]
get_ipython().run_line_magic('cat', 'child_process.py')
from telnetlib import Telnet
get_ipython().run_line_magic('pinfo', 'Telnet')
import pexpect
ftp = pexpect.spawn("ftp ftp.chandrashekar.info")
ftp
r = ftp.expect(r"Name .+: ")
r
ftp.before
ftp.after
ftp.sendline("testuser")
ftp.expect("Password: ")
ftp.before
ftp.after
ftp.sendline("w3lc0me")
ftp.expect("f")
f.before
f.after
ftp.before
ftp.after
ftp.sendline("cd /www/files")
ftp.expect("sdfsdfd")
ftp.expect("sdfsdfd", 5)
get_ipython().run_line_magic('pinfo', 'pexpect.spawn')
ftp.expect("ftp> ", 5)
ftp.before
ftp.after
ftp.sendline("binary")
ftp.sendline("passive")
ftp.before
ftp.expect("ftp> ")
ftp.before
ftp.expect("ftp> ")
ftp.before
ftp.sendline("get xml.zip")
ftp.expect("ftp> ")
ftp.before
ftp.expect(["sh> ", "ftp> ", "telnet> "])
ftp.sendline("binary")
ftp.expect(["sh> ", "ftp> ", "telnet> "])
ftp.interact()
import collections
collections.abc
collections.abc.Sequence
from ftplib import FTP
get_ipython().run_line_magic('pinfo', 'FTP')
ftp = FTP("ftp.chandrashekar.info", "testuser", "w3lc0me")
ftp
ftp.cwd("/www/files")
ftp.dir()
ftp.listdir()
ftp.nlst()
ftp.nlst()
ftp.dir()
