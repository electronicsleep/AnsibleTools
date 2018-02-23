#!/usr/bin/env python

# Author: https://github.com/electronicsleep
# Date: 02/22/2018
# Purpose: Using Ansible and Python for more control
# Released under the BSD license

import subprocess

user = "ubuntu"

hosts_file = open("/etc/ansible/hosts", "r")

host_num = 0
for host_line in hosts_file:
    if "[" in host_line:
        group = host_line
        print("Group: ", host_line.strip())
    elif host_line != "":
        host_num += 1
        print("Host Details:", host_line.strip())
        print("Host Num:", host_num)
        host = host_line.split(" ")[0]
        print("Address:", host)
        host_one = open("ansible_host", 'w')
        host_one.write("[default]\n")
        host_one.write(host + "\n")
        host_one.close()

        output = subprocess.check_output(['ansible-playbook', 'check-disk.yml', '-i', "ansible_host", "-u", user])
        for line in output.decode("utf-8").split("\n"):
            print(line.strip())
