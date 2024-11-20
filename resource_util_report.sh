#Purpose: Generate a report of CPU, RAM, and storage utilization for a project.

#!/bin/bash

source ~/openstack_credentials.sh
echo "Resource Utilization Report:"
echo "=========================="
openstack usage show --start $(date -d '1 month ago' +%Y-%m-%d) --end $(date +%Y-%m-%d)
