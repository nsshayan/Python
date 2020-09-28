from pssh.utils import load_private_key
from pssh.clients import ParallelSSHClient
import yaml


with open("host_config.yml") as yaml_file:
    host_config = yaml.load(yaml_file, Loader=yaml.CLoader)

hosts = list(host_config.keys())
print(hosts)

client = ParallelSSHClient(hosts, host_config=host_config)
commands = ("uptime", "whoami", "date", "uname", "id", "hostname", "pwd")

#output = client.run_command('%s', host_args=commands)
output = client.run_command("uptime")
dirs = ("one", "two", "three", "four", "five", "six", "seven")
output = client.run_command('mkdir /tmp/%s', host_args=dirs)

for host, host_output in output.items():
    for line in host_output.stdout:
        print(host, line)
