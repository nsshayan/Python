from subprocess import Popen, PIPE


def get_ip_linux():
    with Popen("ifconfig", stdout=PIPE, encoding="utf8") as p:
        # for line in p.stdout:
        #    if "inet " in line:
        #        print(line.split()[1])

        return [line.split()[1] for line in p.stdout if "inet " in line]


if __name__ == "__main__":
    print(get_ip_linux())

