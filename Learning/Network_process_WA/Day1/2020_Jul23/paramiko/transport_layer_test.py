#!/usr/bin/env python
from paramiko import Transport

try:
    transport = Transport(("dhrona.net", 12276))

    transport.connect(username="user10", password="welcome")

    channel = transport.open_channel("session")
    channel.exec_command("cat /etc/passwd")

    instream = channel.makefile("r")
    for line in instream:
        print(line.strip().upper())

except Exception as e:
    print("Caught some exception: ", e)
finally:
    instream.close()
    channel.close()
    transport.close()
