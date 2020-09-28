from run_and_parse_output import run_command

ip_regex = "\d{1,3}(\.\d{1,3}){3}"

for match in run_command("/sbin/ifconfig", ip_regex):
    print(match.group())
