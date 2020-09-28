from run_and_parse_output import run_command

ip_regex = r"\d+$"

for match in run_command("./dummy_script.py", ip_regex):
    print(match.group())
