import yaml
import pexpect
import sys

def pexpect_session(yaml_file, out):
    with open(yaml_file) as infile:
        config = yaml.load(infile,  Loader=yaml.CLoader) 

    proc = pexpect.spawn(config["command"], encoding="utf8")
    for prompt, reply in config["session"].items():
        if isinstance(reply, list):
            for r in reply:
                proc.expect(prompt)
                msg = proc.before
                out.write(msg)
                proc.sendline(r)
        else:
            proc.expect(prompt)
            msg = proc.before
            out.write(msg)
            proc.sendline(reply)

if __name__ == '__main__':
    pexpect_session("telnet_session.yml", sys.stdout)