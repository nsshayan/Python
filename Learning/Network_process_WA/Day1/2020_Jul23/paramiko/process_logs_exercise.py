
ssh_info = {
    "192.168.56.101": {
        "username": "root",
        "password": "welcome",
        "logfiles": [("/var/log/pacman.log", r"error"),
                     ("/var/log/system.log", r"\d+(\.\d+){3}")]
    },

    "192.168.56.102": {
        "username": "root",
        "password": "welcome",
        "logcommands": [("/usr/bin/dmesg", r"error"),
                        ("/usr/bin/journalctl -f", r"dhcp")]

    }

}


def process_logs(info):
    from ssh_connection import SSHConnection
    import re

    for host, host_info in info.items():
        with SSHConnection(host,
                           host_info["username"],
                           host_info["password"]) as conn:
            if "logfiles" in host_info:
                for path, regex in host_info["logfiles"]:
                    pattern = re.compile(regex)
                    with conn.open(path) as infile:
                        for line in infile:
                            matches = pattern.finditer(line)
                            if matches:
                                for m in matches:
                                    yield m

            if "logcommands" in host_info:
                for command, regex in host_info["logcommands"]:
                    pattern = re.compile(regex)
                    _, stdout, _ = conn.exec_command(command)
                    for line in stdout:
                        matches = pattern.finditer(line)
                        if matches:
                            for m in matches:
                                yield m


if __name__ == '__main__':
    for match in process_logs(ssh_info):
        print(match.string)
