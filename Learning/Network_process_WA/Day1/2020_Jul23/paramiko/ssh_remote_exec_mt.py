from gevent import monkey
monkey.patch_all()

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
                "run": "hostname",
                "stdout": "./hostname.out"
            },
            {
                "run": "ls -l /usr /sdfsf /boot",
                "stdout": "./ls.out",
                "stderr": "./ls.err"
            },
            {
                "parse": ["/var/log/messages", "/var/log/system.log"],
                "match": r"\d+",
                "process": "print"
            }
        ]
    },

    "192.168.56.102": {
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
        from threading import Thread
        from queue import Queue
        self.conn_thread = Thread(target=self.execute)
        self.queue = Queue(10)

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

    def __enter__(self):
        self.connect()
        self.quit = False
        self.conn_thread.start()
        return self

    def __exit__(self, et, ev, tb):
        self.quit = True
        self.queue.put((None, None, None, None))
        self.conn_thread.join()
        self.close(et, ev, tb)

    def run(self, run, stdin=None, stdout=None, stderr=None):
        self.queue.put((run, stdin, stdout, stderr))

    def execute(self):
        while True:
            command, stdin, stdout, stderr = self.queue.get()
            if command is None and self.quit is True:
                break

            instream, outstream, errstream = self.client.exec_command(command)

            if stdin:
                with open(stdin) as infile:
                    for line in infile:
                        instream.write(line)
                        instream.flush()

            if stdout:
                with open(stdout, "w") as outfile:
                    for line in outstream:
                        outfile.write(line)

            if stderr:
                with open(stderr, "w") as errfile:
                    for line in errstream:
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
