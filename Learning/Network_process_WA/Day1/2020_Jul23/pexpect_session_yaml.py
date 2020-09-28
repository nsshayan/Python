
def pexpect_session(yaml_file, output):
    import pexpect
    import yaml

    with open(yaml_file) as infile:
        session_config = yaml.load(infile)

    child = pexpect.spawn(session_config["command"])

    expected_prompts = list(session_config["session"].keys())

    while True:
        try:
            index = child.expect(expected_prompts)
            prompt = expected_prompts[index]
            print(f"Got {prompt}")
            reply = session_config["session"][prompt]
            if isinstance(reply, list):
                for command in reply:
                    print(f"Sending {command}")
                    child.sendline(command)
                    child.expect(prompt)
                    print(str(child.before, "utf8"), file=output)
                    if command == "exit":
                        break
            elif isinstance(reply, str):
                print(f"Sending -> {reply}")
                child.sendline(reply)
        except pexpect.EOF:
                print("Closed connection...")
                break

if __name__ == '__main__':
    import sys
    pexpect_session("telnet_session.yml", sys.stdout)

