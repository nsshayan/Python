#!/anaconda3/bin/python3
from coapthon.client.helperclient import HelperClient

host = "10.106.224.142"
port = 4035	
path ="basic"

client = HelperClient(server=(host, port))
response = client.get(path)
print(response.pretty_print())
client.stop()
