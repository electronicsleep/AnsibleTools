#!/usr/bin/env python
# Author: https://github.com/electronicsleep
# Purpose: Using Ansible and Python for more control
# Released under the BSD license

import subprocess
import argparse
import datetime
from termcolor import colored

date = datetime.datetime.now().strftime("%Y%m%d-%H%M")
print("report date: " + date)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--playbook", help="playbook to run", required=False)
    parser.add_argument("-u", "--user", help="user for host", required=False)
    parser.add_argument("-v", "--verbose", help="numeric verbose", required=False)
    args = parser.parse_args()

    if args.playbook is None:
        playbook = "check-disk.yml"
    else:
        playbook = args.playbook

    if args.user is None:
        user = "ubuntu"
    else:
        user = args.user

    if args.verbose is None:
        verbose = 0
    else:
        verbose = int(args.verbose)

    if verbose > 0:
        print("verbose: ", verbose)
        print("playbook: ", playbook)
        print("user: ", user)

    log_file = "reports/report-" + date + ".log"
    hosts_file = open("/etc/ansible/hosts", "r")
    report = open(log_file, 'w')

    disk_space_check = []
    for size in range(80, 100):
        disk_space_check.append(str(size) + "%")

    found_host_issue = []
    host_num = 0
    for host_line in hosts_file:
        if "[" in host_line:
            group = host_line
            if verbose > 0:
                print("Group: ", group)
        elif host_line != "":
            host_num += 1
            print("### Host Num:", host_num)
            print("Host Details:", host_line.strip())
            host = host_line.split(" ")[0]
            print("Address:", host)
            host_one = open("ansible_host", 'w')
            host_one.write("[default]\n")
            host_one.write(host + "\n")
            host_one.close()

            output = subprocess.check_output(['ansible-playbook', playbook, '-i', "ansible_host", "-u", user])
            report.write("Host Details: " + host_line)
            for line in output.decode("utf-8").split("\n"):
                if verbose > 0:
                    print(line.strip())
                for disk_space in disk_space_check:
                    if disk_space in line:
                        if verbose > 0:
                            print("Found: ", disk_space)
                        found_host_issue.append(host_line)

                report.write(line + "\n")

    if len(found_host_issue) == 0:
        print_warn("No issues found")
    for host in found_host_issue:
        print_error("Issue: " + host)
    print("Wrote Log: " + log_file)
    report.close()


def print_error(message):
    print(colored(message, 'red'))


def print_warn(message):
    print(colored(message, 'yellow'))

if __name__ == '__main__':
    main()
