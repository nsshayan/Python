from run_commands import parse_command_output

extraction_dict = {
   "ipv4_addr": """\d{1,3}      # Match first octet
                 (\.\d{1,3})    # Match next 3 octets with . prefix
                 {3}"""

}

if __name__ == '__main__':
    for key, match in parse_command_output("/sbin/ifconfig", extract=extraction_dict):
        print(key, match.group()) # --> ipv4_addr 192.168.56.105