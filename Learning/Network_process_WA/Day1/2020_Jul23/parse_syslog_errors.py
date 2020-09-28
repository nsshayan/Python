from run_and_extract import run_command

extract = {
    "error": "error",
    "ip_addrs": "\d{1,3}(\.\d{1,3}){3}",
    "interface_message": r"\ben\d\b"
}

for n, key, match in run_command("tail -f /var/log/system.log", extract):
    print(n, key, match.string)
