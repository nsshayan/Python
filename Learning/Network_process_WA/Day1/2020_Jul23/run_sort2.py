from subprocess import Popen, PIPE

with Popen("sort", stdin=PIPE, encoding="utf8") as sort_proc:
        while True:
            line = input("Enter line: ")
            if not line: break
            sort_proc.stdin.write(line + "\n")
