#!/bin/bash
# Author: https://github.com/electronicsleep
# Date: 07/20/2017
# Purpose: Ansible - Check os updates and log details to a file and upgrade
# Released under the BSD license

DATE=$(date +%Y-%m-%d)
echo "DATE: $DATE" | tee /tmp/apt-update-$DATE.log
# Run Updates and save to file
sudo apt-get update ; sudo apt-get upgrade --dry-run | tee -a /tmp/apt-update-$DATE.log
if grep "^0 upgraded, 0 newly installed, 0 to remove" /tmp/apt-update-$DATE.log; then
	echo "### NO UPDATES ###" | tee -a  /tmp/apt-update-$DATE.log
else
  # Create update log by timestamp if updates
  echo "### UPDATES PENDING ###" | tee -a /tmp/apt-update-$DATE.log
fi
