#Purpose: Apply metadata tags to multiple instances.

#!/bin/bash

source ~/openstack_credentials.sh
instances=$(openstack server list -f value -c ID)

for instance in $instances; do
  echo "Tagging instance $instance with 'environment=production'"
  openstack server set --property environment=production $instance
done
