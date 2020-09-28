from getpass import getpass
import logging
import sys
from telnetlib import Telnet
import re
from time import sleep

HOST = "192.168.57.101"
user = "joe" 
password = "w3lc0me" 

tn = Telnet(HOST)
#tn.set_debuglevel(7)
logging.basicConfig(filename='telnet_session.log',level=logging.DEBUG)

logging.info("Expecting login prompt")
tn.read_until("login: ")
tn.write(user + "\r")
logging.info("Sent username")

logging.info("Expecting password")
tn.read_until("Password:", timeout=5)
tn.write(password + "\r")
logging.info("Sent password")

logging.info("Expecting ? prompt")
tn.read_until("?", timeout=5)
tn.write("vt100\r")
logging.info("Sent terminal type")

logging.info("Expecting shell prompt")
tn.read_until(r"> ")
tn.write("uname -a\r")
logging.info("Sent 'uname -a' command")

logging.info("Expecting shell prompt")
print("OUTPUT: ", tn.read_until(r"> "))

tn.write("exit\r")
logging.info("Exiting")


