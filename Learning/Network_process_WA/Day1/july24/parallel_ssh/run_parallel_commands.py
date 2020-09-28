from pssh.utils import load_private_key
from pssh.clients import ParallelSSHClient

host_config = {'192.168.56.105' : {
                        'user': 'root',
                        'password': 'welcome',
                        'port': 22,
                        },

             "192.168.1.130": {
                        'user': 'user01',
                        'password': 'w3lc0me',
                        'port': 22
             },

             "192.168.1.32": {
                        'user': 'pythonista',
                        'password': 'guido123',
                        'port': 22
                        #'pkey': load_private_key("/Users/chandrashekar/.ssh/id_rsa")
             }
}

hosts = list(host_config.keys())

client = ParallelSSHClient(hosts, host_config=host_config)
output = client.run_command('%s', host_args=["uptime", "date", "uname -a"])
for host, host_output in output.items():
    for line in host_output.stdout:
        print(host, line)
