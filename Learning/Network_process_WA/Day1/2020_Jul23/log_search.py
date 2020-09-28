config = {
    "192.168.56.101" : ["/var/log/system.log", "/var/log/messages"],
    "192.168.56.102" : ["/var/log/journal.log", "/var/log/syslog"]
}

def search_log(pattern, config):
    pass


if __name__ == '__main__':
    for host, filename, line in search_log("Authentication failure.+", config):
        print("{}:{}:{}".format(host, filename, line))
