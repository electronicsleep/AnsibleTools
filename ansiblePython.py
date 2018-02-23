#!/usr/bin/env python

# Author: https://github.com/electronicsleep
# Date: 02/22/2018
# Purpose: Using Ansible and Python for more control
# Released under the BSD license

import subprocess
import argparse

import datetime
date = datetime.datetime.now().strftime("%Y%m%d-%H%M")
print("date: " + date)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--playbook", help="playbook to run", required=False)
    args = parser.parse_args()

    if args.playbook is None:
        playbook = "check-disk.yml"
    else:
        playbook = args.playbook

    print("playbook: ", playbook)
    user = "ubuntu"

    hosts_file = open("/etc/ansible/hosts", "r")
    report = open("report-" + date + ".log", 'w')

    host_num = 0
    for host_line in hosts_file:
        if "[" in host_line:
            group = host_line
            print("Group: ", group)
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

            output = subprocess.check_output(['ansible-playbook', playbook, '-i', "ansible_host", "-u", user])
            report.write("Host Details: " + host_line)
            for line in output.decode("utf-8").split("\n"):
                print(line.strip())
                report.write(line + "\n")

    report.close()


if __name__ == '__main__':
    main()
