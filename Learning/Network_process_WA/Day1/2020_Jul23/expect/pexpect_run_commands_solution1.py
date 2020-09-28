import pexpect

def run_child_process(command):
        child = pexpect.spawn(command["program"])
        for expected, cmd in command["commands"]:
            if type(cmd) is str:
                child.expect(expected)
                child.sendline(cmd)
            elif type(cmd) is list:
                for c in cmd:
                    child.expect(expected)
                    child.sendline(c)
    
def run_commands(commands):
    from threading import Thread
    for command in commands:
        #run_child_process(command)                    
        t = Thread(target=run_child_process, args=(command,))
        t.start()
        
        
if __name__ == '__main__':
    import yaml
    with open("commands.yml") as infile:
        run_commands(yaml.load(infile))
