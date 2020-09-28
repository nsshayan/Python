from paramiko import SSHClient, AutoAddPolicy
from threading import Thread

import logging
logging.basicConfig(filename="run_bc.log")
log = logging.getLogger("paramiko")
log.setLevel(logging.DEBUG)

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())



client.connect('192.168.56.101', username='root', password='welcome')
stdin, stdout, stderr = client.exec_command('bc')

def send_command(out):
    while True:
        line = input("Enter command: ")
        out.write(line + "\n")

def get_result(instream):
    for line in instream:
        print(line, flush=True)


t1 = Thread(target=send_command, args=(stdin,))
t2 = Thread(target=get_result, args=(stdout,))
t1.start()
t2.start()

t1.join()
t2.join()
client.close()

