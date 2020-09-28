#!/usr/bin/env python
from subprocess import Popen, PIPE

def read_chunk(stream, size):
    while True:
        data = stream.read(size)
        if not data: break
        yield data


with Popen("./progress_test.sh", stdout=PIPE) as progress:
    for v in read_chunk(progress.stdout, 2):
        print(str(v, "utf8"), end="", flush=True)

