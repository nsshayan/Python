from pssh.clients import ParallelSSHClient
import yaml
from yaml import CLoader

with open("host_config_commands.yml") as infile:
        hc = yaml.load(infile, Loader=CLoader)

client = ParallelSSHClient(hc["config"].keys(), host_config=hc["config"])


for commands in zip(*hc["commands"].values()):
    output = client.run_command("%s", host_args=commands)
    for host, host_output in output.items():
        for line in host_output.stdout:
            print(host, line)
