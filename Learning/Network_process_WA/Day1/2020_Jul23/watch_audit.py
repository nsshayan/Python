from run_and_parse_output import run_command

ip_regex = r"\d{1,3}(\.\d{1,3}){3}"

for match in run_command("cat /var/log/system.log", ip_regex):
    print(match.string)
