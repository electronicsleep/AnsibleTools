#!/bin/bash

# Author: https://github.com/electronicsleep
# Date: 07/20/2017
# Purpose: Ansible - Bootstrap Host 
# Released under the BSD license

HOST=$(cat new_host.txt | cut -f 1 -d ' ')
PEM=""

if [ -z $HOST ];then
 echo "ERROR: Please set HOST"
 exit 1
fi

if [ -z $PEM ];then
 echo "ERROR: Please set PEM"
 exit 1
else
 echo "HOST: $HOST"
 cat ~/.ssh/id_rsa.pub | ssh -i $PEM ubuntu@$HOST "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
 # Ensure Python installed for Ansible
 ssh ubuntu@$HOST 'sudo apt-get install python3 -y'
 ssh ubuntu@$HOST 'sudo apt-get install python -y'
fi
exit 0
