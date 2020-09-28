from paramiko_connection import SSHConnection
#from pssh_connection import SSHConnection
from ssh_session import SSHSession
from argparse import ArgumentParser

program_help = """A simple program to run a series of commands on a remote host
via SSH protocol. The host to connect and the series of commands to run will be
sourced via yaml file.
"""

if __name__ == '__main__':
    parser = ArgumentParser(description=program_help)
    parser.add_argument("yaml_path", help="Path to yaml file")
    args = parser.parse_args()

    ssh_session = SSHSession(SSHConnection, args.yaml_path)
    ssh_session.run()
