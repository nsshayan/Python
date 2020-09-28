import pexpect
from pexpect import TIMEOUT
from getpass import getpass
from sys import argv

import logging
logging.basicConfig(level=logging.INFO)
from logging import debug, info, warn, error

if len(argv) < 2:
    password = getpass("Enter password: ")
else:
    password = argv[1]

with open("ftp.log", "wb") as outfile:
    info("Connecting...")
    child = pexpect.spawn('ftp ftp.chandrashekar.info', logfile=outfile)
    child.expect('Name .*: ')

# r = child.expect(['Name .*: ', 'Error .*', 'Redirecting .*'])
# if r == 0:
    # got name
#    pass
#  elif r == 1:

    debug("Sending username...")
    child.sendline('testuser')

    child.expect('Password:')
    debug("Sending password...")
    child.sendline(password)

    child.expect('ftp> ')
    debug("Sending 'cd /www/files/python'")
    child.sendline('cd /www/files/python')

    child.expect('ftp> ', timeout=20)
    debug("Downloading file...")
    child.sendline('get users.txt')

    try:
        child.expect('ftp> ', timeout=20)
        debug("Exiting...")
        child.sendline("quit")
    except TIMEOUT as e:
        error("Timeout occurred while downloading...")

info("Download complete...")
#child.interact()

