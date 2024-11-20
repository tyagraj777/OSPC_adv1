#Purpose: Automatically update DNS records when a floating IP is assigned to an instance.

import os
import subprocess
import requests

os.system("source ~/openstack_credentials.sh")

instance_id = "<INSTANCE_ID>"
floating_ip = subprocess.check_output(f"openstack server show {instance_id} -f value -c addresses", shell=True).decode().strip().split("=")[1]

dns_record = {"type": "A", "name": "instance.mydomain.com", "content": floating_ip, "ttl": 300}
requests.put("https://api.mydnsprovider.com/v1/records", json=dns_record, headers={"Authorization": "Bearer YOUR_API_KEY"})
print(f"DNS updated with floating IP: {floating_ip}")
