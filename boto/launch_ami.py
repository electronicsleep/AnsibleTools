#!/usr/bin/env python

# Author: https://github.com/electronicsleep
# Date: 07/20/2017
# Purpose: Launch Ubuntu 16 LTS instance in EC2
# Released under the BSD license

import boto3
import pprint
import time

# Ubuntu 16 LTS
ami = 'ami-09d2fb69'

# Enter Security group and Subnet
sg = ['sg-12345678']
sn = 'subnet-12345678'

client = boto3.client('ec2', 'us-west-1')

response = client.run_instances(ImageId=ami, MinCount=1, MaxCount=1, InstanceType='t2.micro', SubnetId=sn, SecurityGroupIds=sg, KeyName='default')

instance_id = response['Instances'][0]['InstanceId']

instance_id_start = []
instance_id_start.append(instance_id)

print("instance_id: ", instance_id)

pprint.pprint(response)

print("#" * 10)

time.sleep(5)

for wait in range(0, 1000):

    response2 = client.describe_instances(InstanceIds=instance_id_start)

    for r in response2['Reservations']:
        for inst in r['Instances']:
            print("%s %s" % (inst['InstanceId'], inst['State']['Name']))

    if inst['State']['Name'] == 'running':
        print("Instance Running")
        break
    else:
        print("Waiting for instsance to launch:", wait)
        time.sleep(5)

print("#" * 10)

tag = client.create_tags(Resources=[instance_id], Tags=[{'Key': 'Name', 'Value': 'NEW_INSTANCE'}])

pprint.pprint(tag)

print("#" * 10)

print("\nEC2 Instance launched:", inst['InstanceId'], "Tagged", 'NEW_INSTANCE\n')

exit(0)
