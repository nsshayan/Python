home_machines_config = {
 "192.168.1.130": {"user": "user01", "password": "tuxedo", "port": 22},
 "192.168.1.32": {"user": "pythonista", "password": "guido123", "port": 22},
 "192.168.1.7": {"user": "root", "password": "welcome", "port": 22},
 }

from pssh.clients import ParallelSSHClient

client = ParallelSSHClient(home_machines_config.keys(), host_config=home_machines_config)

for host, output in client.run_command("df -h").items():
    print("-" * 60)
    print("===== Host", host, "=====")
    print("-" * 60)
    print("\n".join(output.stdout))

# To run different commands on each host:
out = client.run_command("%s %s", host_args=(
                                    ("mkdir", "/tmp/one"),
                                    ("rmdir", "/tmp/two"),
                                    (": ", ""),  # Ignore this host
                                    ("cat", "/etc/passwd")))
