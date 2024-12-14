#!/usr/bin/env python

# Author: https://github.com/electronicsleep
# Date: 07/20/2017
# Purpose: Generate Ansible Inventory
# Released under the BSD license

import boto3
client = boto3.client('ec2', 'us-west-1')
response = client.describe_instances()
print("[default]")
for r in response['Reservations']:
    for inst in r['Instances']:
        if inst['State']['Name'] == 'running':
            print("%s # %s %s %s" % (inst['PublicIpAddress'], inst['InstanceId'], inst['Tags'][0]['Value'], inst['State']['Name']))
