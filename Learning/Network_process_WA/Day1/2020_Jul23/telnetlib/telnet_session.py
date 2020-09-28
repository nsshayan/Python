from time import sleep


def run_telnet_session(session_yaml_file, outstream):
    from telnetlib import Telnet
    import yaml

    with open(session_yaml_file) as infile:
        session_config = yaml.load(infile)

    tn = Telnet(host=session_config["host"], port=session_config["port"])

    #tn.set_debuglevel(7)

    output = {}
    expected_prompts = [bytes(prompt, "utf8") \
              for prompt in session_config["session"].keys()]

    commands = session_config["session"]

    while True:
        index, match, text = tn.expect(expected_prompts)
        cmd = commands[str(expected_prompts[index], "utf8")]
        if isinstance(cmd, str):
            tn.write(bytes(cmd + "\r", "utf8"))
            output[expected_prompts[index]] = text

        elif isinstance(cmd, list):
            output[expected_prompts[index]] = {}
            for c in cmd:
                tn.write(bytes(c + "\r", "utf8"))
                result = tn.read_until(expected_prompts[index])
                output[expected_prompts[index]][c] = result
                if c == "exit":
                    break

        print(output, file=outstream)


if __name__ == '__main__':
    import sys

    run_telnet_session("telnet_session.yml", sys.stdout)
