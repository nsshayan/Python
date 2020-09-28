from gevent import monkey; monkey.patch_all()

from ssh_util import ssh_connect
from threading import Thread

commands = [
    "ls -lR /usr/local",
    "find /usr/local/build/busybox",
    "journalctl -n 1000"
]

def get_output(comm, stream):
    for line in stream:
        print(f"{comm}: {line.strip()}")

def joinall(threads):
    from collection import deque
    from sys import getswitchinterval

    interval = getswitchinterval()
    threads = deque(threads)

    while threads:
        t = threads[0]
        t.join(timeout=interval)
        if not t.is_alive():
            threads.popleft()
            yield t
        else:
            threads.rotate(-1)


client = ssh_connect("192.168.56.105", "root", "welcome")
threads = []

for comm in commands:
    _, stdout, _ = client.exec_command(comm)
    t = Thread(target=get_output, args=(comm, stdout))
    threads.append(t)
    t.start()

for t in joinall(threads):
    print(f"-------------------- {t.name} finished ------------------------")

client.close()
