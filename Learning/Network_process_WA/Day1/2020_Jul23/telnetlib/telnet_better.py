
shell_prompt = "[root@archvm ~]# "

commands = {
    "login":  "root",
    "Password": "welcome",
    "[root@archvm ~]# ":  ("whoami", "uname -a", "ls /etc", "exit")
}

def run_commands(hostname, commands, generator=True):
    from telnetlib import Telnet
    from time import sleep

    host = Telnet(hostname)

    if not generator: result = {}
    command = None

    for key, value in commands.items():
        if type(value) is str:
            if command is not None:
                if not generator:
                    result[str(command, "utf8")] = output
                else:
                    yield str(command, "utf8"), output
            prompt = bytes(key, "utf8")
            command = bytes(value, "utf8")
            output = str(host.read_until(prompt), "utf8")
            host.write(command + b"\r")
        elif type(cmd) in list:
            for c in cmd:
                output.append(str(host.read_until(prompt), "utf8"))
                host.write(c + b"\r")
    return output

out = run_commands("192.168.56.101", commands)
for o in out:
    print(o)
    print("----------------------------------")


