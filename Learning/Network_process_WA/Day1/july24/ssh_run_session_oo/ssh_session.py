class SSHSession:
    def __init__(self, SSHConnection, session):
        if not isinstance(session, dict):

            import yaml
            if hasattr(session, "read") and callable(getattr(session, "read")):
                self.session = yaml.load(session, Loader=yaml.CLoader)
            elif isinstance(session, str):
                with open(session) as session_file:
                    self.session = yaml.load(session_file, Loader=yaml.CLoader)
            else:
                raise TypeError("session parameter must be either dict, file or str")

        else:
            self.session = session

        self.ssh = SSHConnection(host=self.session["host"],
                                 port=self.session.get("port", 22),
                                 username=self.session["user"],
                                 password=self.session.get("password"),
                                 pkey=self.session.get("pkey"))

    def run(self):
        import shlex
        for command in self.session["session"]:
            args = shlex.split(command)
            comm = args.pop(0).lower()
            self.ssh._execute(comm, *args)

if __name__ == '__main__':
    from paramiko_connection import SSHConnection
    ssh_session = SSHSession(SSHConnection, "ssh_transcript.yml")
    ssh_session.run()


