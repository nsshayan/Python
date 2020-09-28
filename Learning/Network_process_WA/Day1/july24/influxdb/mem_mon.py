#!/usr/bin/env python

from sshconn import SSHConnection

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("host",
            help="Remote hostname/ip address")

    parser.add_argument("user",
            help="Remote username")

    parser.add_argument("pid",
            help="PID of remote process")

    args = parser.parse_args()


    print(f"{args.pid},host={args.host} ", end="")
    with SSHConnection(args.host, args.user) as conn:
        out, err = conn.run_command(f"grep ^Vm /proc/{args.pid}/status")
        #for line in out.splitlines():
        #    name, value = line.split()[:2]
        #    name = name.strip(":").lower()
        #    print(f"{name}={value}, ", end="")
        result = ",".join([ f"{name.strip(':').lower()}={value}" \
                             for name, value in \
                             [ line.split()[:2] for line in out.splitlines() ]])

    print(result)

