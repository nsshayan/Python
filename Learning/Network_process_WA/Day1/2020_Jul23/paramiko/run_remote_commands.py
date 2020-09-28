def parse_config(filename):
    config = []
    with open(filename) as config_file:
        for line in config_file:
            line = line.strip()
            if not line or line.startswith("#"): continue
            args = line.split()
            command = args.pop(0)
            config.append((command, args))
    return config


class SSHConnection:

    def connect(self, host, username, password):
        from paramiko import SSHClient, AutoAddPolicy
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.client.connect(host, username=username, password=password)
        self.sftp = self.client.open_sftp()

    def run(self, *args):
        self.client.exec_command(*args)




def invalid_command(*args):
    print("Invalid command...")

if __name__ == '__main__':
    config = parse_config("paramiko_commands.lst")

    ssh = SSHConnection()

    ssh_commands = {
        "CONNECT": ssh.connect,
        "RUN"    : ssh.run,
    }

    for command, args in config:
        if command in ssh_commands:
            ssh_commands[command](*args)
        else:
            getattr(ssh.sftp, command.lower())(*args)
