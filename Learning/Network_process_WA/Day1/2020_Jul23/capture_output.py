from gevent import monkey
monkey.patch_all()

from threading import Thread
from queue import Queue

def process_command(cmd, record, result_queue):
    from subprocess import Popen, PIPE
    p = Popen(record["command"], 
              encoding="utf8", stdout=PIPE)
    for line in p.stdout:
        for name, pattern in record.items():
            if name == "command": continue
            for m in pattern.finditer(line):
                key = f"{cmd}:{record['command']}:{name}"
                #yield {key: m}
                result_queue.put({key: m})


def capture_output(yaml_file):
    import yaml
    import re

    with open(yaml_file) as infile:
        config = yaml.load(infile)
    
    results = Queue(64*1024)
    workers = []

    for cmd_name, record in config.items():
        record = { k: re.compile(v) if k != "command" else v \
                   for k, v in record.items() }

        p = Thread(target=process_command, 
                   args=(cmd_name, record, results))
        p.start()
        workers.append(p)

    while True:
        yield results.get()

 
if __name__ == '__main__':

    for command in capture_output("cmdlist.yml"):
        for result in command:
            print(result)
        # {"ipaddr:ifconfig:ipv4-pattern": <match object>}
