#Purpose: Monitor hypervisors for failed instances and migrate them.

import os
import subprocess

os.system("source ~/openstack_credentials.sh")

failed_hypervisors = subprocess.check_output("openstack hypervisor list -f value -c 'Hypervisor Hostname' -c 'State'", shell=True).decode().splitlines()
for hypervisor in failed_hypervisors:
    hostname, state = hypervisor.split()
    if state.lower() != 'up':
        print(f"Detected failure on hypervisor {hostname}. Migrating instances...")
        os.system(f"openstack server migrate --live {hostname}")
