#Purpose: Scale worker nodes dynamically based on pod utilization.

import os
import subprocess
import json

os.system("source ~/openstack_credentials.sh")

# Check Kubernetes pod utilization
kube_stats = subprocess.check_output("kubectl get pods -o json", shell=True)
pods = json.loads(kube_stats)
pending_pods = len([pod for pod in pods['items'] if pod['status']['phase'] == 'Pending'])

# Scale OpenStack instances
if pending_pods > 5:
    print("Scaling up Kubernetes worker nodes...")
    os.system("openstack server create --image <IMAGE> --flavor <FLAVOR> --network <NETWORK> kube-worker")
else:
    print("No scaling required.")
