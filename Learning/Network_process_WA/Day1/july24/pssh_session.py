from pssh.clients import ParallelSSHClient
import yaml
from yaml import CLoader

with open("host_config.yml") as infile:
        hc = yaml.load(infile, Loader=CLoader)

client = ParallelSSHClient(hc.keys(), host_config=hc)
output = client.run_command("uptime")

for host, host_output in output.items():
    for line in host_output.stdout:
        print(host, line)

output = client.run_command("%s", host_args=("uptime", "uname -a"))
for host, host_output in output.items():
    for line in host_output.stdout:
        print(host, line)

output = client.run_command("cat %s", host_args=("/etc/passwd", "/etc/hosts"))
for host, host_output in output.items():
    for line in host_output.stdout:
        print(host, line)
