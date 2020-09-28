from telnetlib import Telnet


HOST = "192.168.56.101"
user = "root"
password = "welcome"

shell_prompt = "[root@archvm ~]#"

commands = {
    "archvm login: " : user,
    "Password: "     : password,
    shell_prompt     : ["whoami", "uname -a", "ls /etc", "exit"]
}

def run_commands(host, commands):
    expected_prompts = [ bytes(p, "utf8") for p in commands.keys() ]
    print("EXPECTED PROMPTS: ", expected_prompts)
    while True:
        print("Waiting for prompt...")
        index, match, text = host.expect(expected_prompts)
        cmd = commands[str(expected_prompts[index], "utf8")]
        print(">>> Got {}, selecting {}".format(text, str(cmd)))

        if type(cmd) is str:
            print("--- {} is a string".format(cmd))
            host.write(bytes(cmd + "\r", "utf8"))
            yield (expected_prompts[index], text)

        elif type(cmd) is list:
            print("=== {} is a list".format(str(cmd)))
            for c in cmd:
                print("Sending", c)
                host.write(bytes(c + "\r", "utf8"))
                print("Expecting ", expected_prompts[index])
                result = host.read_until(expected_prompts[index])
                yield {expected_prompts[index] : (c, result)}
                if c == "exit": break

tn = Telnet(HOST)
tn.set_debuglevel(7)

out = run_commands(tn, commands)
for o in out:
    print(">>> Yielded {}".format(str(o)))
    print("----------------------------------")


