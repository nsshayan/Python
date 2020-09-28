from gevent import monkey
monkey.patch_all()

class InvalidCommand(Exception): pass

class SSHConnection:
    def __init__(self, host, port, username, password=None, pkey=None):
        from paramiko import SSHClient, AutoAddPolicy
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.client.connect(hostname=host, port=port,
                            username=username, password=password,
                            key_filename=pkey)
        self.sftp = self.client.open_sftp()

    def exec(self, *args, **kwargs):
        print("Executing command: ", args)
        stdin, stdout, stderr = self.client.exec_command(*args, **kwargs)
        #stdin.close()
        from threading import Thread
        import sys
        stdout_thread = Thread(target=self._copy_output, args=(stdout, sys.stdout))
        stderr_thread = Thread(target=self._copy_output, args=(stderr, sys.stderr))
        stdout_thread.start()
        stderr_thread.start()

    def make_executable(self, path):
        mode = self.sftp.stat(path).st_mode
        return self.sftp.chmod(path, mode | 0o111)

    def exit(self):
        self.sftp.close()
        self.client.close()

    def _copy_output(self, output, to):
        for line in output:
            print(line, file=to, flush=True, end="")
        output.close()

    def _execute(self, command, *args, **kwargs):
        if not command.startswith("_"):
            targets = (self, self.sftp, self.client)
            for t in targets:
                if hasattr(t, command):
                    method = getattr(t, command)
                    if callable(method):
                        return method(*args, **kwargs)
        raise InvalidCommand(f"Invalid command - {command}")
