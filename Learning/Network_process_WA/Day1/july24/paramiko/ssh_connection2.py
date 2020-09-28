class SSHConnection:
    attrs = "open", "get", "put", "chmod", "exec_command", "mkdir", "rmdir"

    def __init__(self, hostname, username, password):
        self.hostname, self.username, self.password = hostname, username, password

        from paramiko import SSHClient, AutoAddPolicy
        self.ssh_client = SSHClient()
        self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())

    def __enter__(self):
        self.ssh_client.connect(
            hostname=self.hostname,
            username=self.username,
            password=self.password)

        self.sftp_client = self.ssh_client.open_sftp()

        return self

    def __getattr__(self, attr):
        if attr not in self.attrs:
            raise AttributeError(
                f"'{self.__class__}' object has no attribute '{attr}'")

        elif hasattr(self.sftp_client, attr):
            return getattr(self.sftp_client, attr)
        elif hasattr(self.ssh_client, attr):
            return getattr(self.ssh_client, attr)

    def __exit__(self, et, ev, tb):
        self.sftp_client.close()
        self.ssh_client.close()

