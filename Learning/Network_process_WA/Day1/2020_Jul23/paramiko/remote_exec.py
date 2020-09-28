#!/usr/bin/env python

class SSHConnection:

    def connect(self, *args, **kwargs):
        print("connect called...")
        input()
        from paramiko import SSHClient, AutoAddPolicy
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())
        self.ssh.connect(*args, **kwargs)
        self.sftp = self.ssh.open_sftp()

    def invalid_command(self, *args, **kwargs):
        print("Invalid command")

    def run_commands(self, config):
        for comm, args, kwargs in config:
            getattr(self, comm)(*args, **kwargs)

    def __getattr__(self, attr):
        print("Processing command:", attr)
        if hasattr(self.ssh, attr):
            return getattr(self.ssh, attr)
        elif hasattr(self.sftp, attr):
            return getattr(self.sftp, attr)
        else:
            return self.invalid_command

def parse_conf(filename):
    from shlex import split
    config = []

    with open(filename) as conf_file:
        for line in conf_file:
            tokens = split(line)
            args = [x for x in tokens[1:] if "=" not in x ]
            kwargs = dict(x.split("=") for x in tokens[1:] if "=" in x)
            config.append([tokens[0], args, kwargs])
    return config


if __name__ == '__main__':
    conn = SSHConnection()
    c = parse_conf("remote_exec.conf")
    conn.run_commands(c)