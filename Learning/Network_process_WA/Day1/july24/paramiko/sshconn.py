class SSHConnection:
    def __init__(self, hostname, username, password):
        pass


    def __enter__(self):
        # connect to remote server
        return self

    def __exit__(self, et, ev, tb):
        # close the connection
        pass

    def run(self, run, stdin=None, stdout=None, stderr=None):
        pass # TODO

