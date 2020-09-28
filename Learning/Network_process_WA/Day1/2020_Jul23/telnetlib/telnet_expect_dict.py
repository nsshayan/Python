from telnetlib import Telnet
from time import sleep

HOST = "192.168.56.101"
user = "root"
password = "welcome"

shell_prompt = "[root@archvm ~]# "

commands = {
    "login"       : user,
    "Password"    : password,
    shell_prompt  : ["whoami", "uname -a", "ls /etc", "exit"]
}

def run_commands(host, commands):
    output = { }
    expected_prompts = [ bytes(p, "utf8") for p in commands.keys() ]

    while True:
        index, match, text = host.expect(expected_prompts)
        cmd = commands[str(expected_prompts[index], "utf8")]
        print(text)

        if type(cmd) is str:
            host.write(bytes(cmd + "\r", "utf8"))
            output[expected_prompts[index]] = text

        elif type(cmd) is list:
            output[expected_prompts[index]] = {}
            for c in cmd:
                host.write(bytes(c + "\r", "utf8"))
                result = host.expect(expected_prompts[index])
                output[expected_prompts[index]][c] = result
                if c == "exit": break

    return output

tn = Telnet(HOST)
tn.set_debuglevel(7)

out = run_commands(tn, commands)
for o in out:
    print(o)
    print("----------------------------------")
