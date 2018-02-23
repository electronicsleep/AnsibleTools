#!/usr/bin/env python

# Author: https://github.com/electronicsleep
# Date: 02/22/2018
# Purpose: Using Ansible and Python for more control
# Released under the BSD license

import subprocess
import argparse
import datetime

date = datetime.datetime.now().strftime("%Y%m%d-%H%M")
print("report date: " + date)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--playbook", help="playbook to run", required=False)
    parser.add_argument("-u", "--user", help="user for host", required=False)
    args = parser.parse_args()

    if args.playbook is None:
        playbook = "check-disk.yml"
    else:
        playbook = args.playbook

    if args.user is None:
        user = "ubuntu"
    else:
        user = args.user

    print("playbook: ", playbook)
    print("user: ", user)

    hosts_file = open("/etc/ansible/hosts", "r")
    report = open("report-" + date + ".log", 'w')

    disk_space_check = []
    for size in range(80, 100):
        disk_space_check.append(str(size) + "%")

    found_host_issue = []
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
                for disk_space in disk_space_check:
                    if disk_space in line:
                        print("Found: ", disk_space)
                        found_host_issue.append(host_line)

                report.write(line + "\n")

    if len(found_host_issue) == 0:
        print("No issues found")
    for host in found_host_issue:
        print("Issue: " + host)

    report.close()


if __name__ == '__main__':
    main()
