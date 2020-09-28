ssh_config = {

    "192.168.56.101": {
        "username": "root",
        "password": "welcome",
        "commands": [
            {
                "run": "uname -a",
                "stdout": "./uname.out"
            },
            {
                "run": "ls -l /usr /sdfsf /boot",
                "stdout": "./ls.out",
                "stderr": "./ls.err"
            }
        ]
    },

    "192.168.56.101": {
        "username": "root",
        "password": "welcome",
        "commands": [
            {
                "run": "uptime",
                "stdout": "./uptime.out"
            }
        ]
    }
}


class SSHConnection:
    def __init__(self, hostname, username, password=None, logfile=None):
        self.hostname = hostname
        self.username, self.password = username, password
        self.logfile = logfile

    def connect(self):
        from paramiko import SSHClient, AutoAddPolicy

        if self.logfile:
            import logging
            logging.basicConfig(filename=self.logfile)
            log = logging.getLogger("paramiko")
            log.setLevel(logging.DEBUG)

        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())

        self.client.connect(self.hostname,
                            username=self.username,
                            password=self.password)

        return self

    def close(self, et=None, ev=None, tb=None):
        self.client.close()

    __enter__, __exit__ = connect, close

    def run(self, run, stdin=None, stdout=None, stderr=None):
        input, output, error = self.client.exec_command(run)

        if stdin:
            with open(stdin) as infile:
                for line in infile:
                    input.write(line)
                    input.flush()

        if stdout:
            with open(stdout, "w") as outfile:
                for line in output:
                    outfile.write(line)

        if stderr:
            with open(stderr, "w") as errfile:
                for line in error:
                    errfile.write(line)


def ssh_remote_exec_old(config):
    for host, settings in config.items():
        ssh = SSHConnection(host, settings["username"], settings["password"])
        ssh.connect()
        for command in settings["commands"]:
            ssh.run(**command)
        ssh.close()


def ssh_remote_exec(config):
    for host, settings in config.items():
        with SSHConnection(host,
                           settings["username"],
                           settings["password"]) as ssh:

            for command in settings["commands"]:
                ssh.run(**command)


if __name__ == '__main__':
    ssh_remote_exec(ssh_config)
