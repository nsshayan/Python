from gevent import monkey
monkey.patch_all()

class InvalidCommand(Exception): pass

class SSHConnection:
    def __init__(self, host, port, username, password=None, pkey=None):
        from pssh.clients import SSHClient
        self.client = SSHClient(host=host, user=username, password=pass,
                                port=port, pkey=pkey)
        self.threads = []

    def exec(self, *args, **kwargs):
        print("Executing command: ", args)
        channel, host, stdout, stderr stdin = self.client.run_command(*args, **kwargs)
        from threading import Thread
        import sys
        stdout_thread = Thread(target=self._copy_output, args=(stdout, sys.stdout))
        stderr_thread = Thread(target=self._copy_output, args=(stderr, sys.stderr))
        stdout_thread.start()
        stderr_thread.start()
        self.threads.append(stdout_thread)
        self.threads.append(stderr_thread)

    def make_executable(self, path):
        ch, host, stdout, stderr, stdin = self.client.run_command(f"chmod +x {path}")
        self.client.close(ch)

    def exit(self):
        for t in self.threads:
            t.join()
        self.client.disconnect()

    def _copy_output(self, output, to):
        for line in output:
            print(line, file=to, flush=True, end="")


    def put(self, *args):
        self.client.scp_send(*args)

    def get(self, *args):
        self.client.scp_recv(*args)

    def _execute(self, command, *args, **kwargs):
        if not command.startswith("_"):
            targets = (self, self.client)
            for t in targets:
                if hasattr(t, command):
                    method = getattr(t, command)
                    if callable(method):
                        return method(*args, **kwargs)
        raise InvalidCommand(f"Invalid command - {command}")
