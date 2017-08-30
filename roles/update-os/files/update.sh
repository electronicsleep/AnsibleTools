#!/bin/bash

# Author: https://github.com/electronicsleep
# Date: 07/20/2017
# Purpose: Ansible - Check Apt updates and log details to a file
# Released under the BSD license

DATE=$(date +%Y%m%d-%H%M)
echo "DATE: $DATE" | tee /tmp/apt-update.log
# Run Updates and save to file
sudo apt-get update ; sudo apt-get upgrade --dry-run | tee -a /tmp/apt-update.log
if grep "0 upgraded, 0 newly installed, 0 to remove" /tmp/apt-update.log; then
	echo "### NO UPDATES ###" | tee -a  /tmp/apt-update.log
else
	echo "### UPDATES PENDING ###" | tee -a /tmp/apt-update.log
fi
# Create update log by timestamp
cat /tmp/apt-update.log > /tmp/apt-update-$DATE.log
