#!/bin/bash
DATE=$(date +%Y%m%d-%H%M)
echo "DATE: $DATE"
sudo apt-get update ; sudo apt-get upgrade --dry-run > /tmp/update_$DATE.log
if grep "0 upgraded, 0 newly installed, 0 to remove" /tmp/update_$DATE.log; then
	echo "*** NO UPDATES ***"
else
	echo "*** UPDATES PENDING ***"
fi