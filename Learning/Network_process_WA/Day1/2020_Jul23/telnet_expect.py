from telnetlib import Telnet

tn = Telnet("192.168.56.105", 2023)
#tn.set_debuglevel(7)

prompts = [b"archvm login: ", b"Password: ", b"\[.+\]\$"]

command = b"uname -a\n"
prompt = b"[pythonista@archvm ~]$"

while True:
    index, match, buffer = tn.expect(prompts)

    if index == 0:
        print("Sending username")
        tn.write(b"pythonista\n")
    elif index == 1:
        print("Sending password")
        tn.write(b"welcome\n")
    else:
        print("Sending command")
        tn.write(command)
        output = tn.read_until(b"$ ")
        output = output.lstrip(command)
        output = output.rstrip(prompt)
        print(str(output, "utf8"))
        break

tn.close()
