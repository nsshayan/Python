from command_utils import run_command

for match in run_command(
                    "ifconfig", 
                    {
                        "ip_address": "\d{1,3}(\.\d{1,3}){3}", 
                         "mac_address": "[0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5}"
                    }):
    # print(match)  # {"ip_address": <re.Match object ...> }
    # print(match["ip_address"].group())  # "192.168.56.101" ...

    if "ip_address" in match:
        print(match["ip_address"].group())
    elif "mac_address" in match:
        print(match["mac_address"].group())