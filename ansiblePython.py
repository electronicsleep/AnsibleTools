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
ssh_private_key = "--private-key=default.pem"
check_disk_name = "/dev/xvda1"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--playbook", help="playbook to run", required=False)
    parser.add_argument("-u", "--user", help="user for host", required=False)
    parser.add_argument("-v", "--verbose", help="numeric verbose", required=False, action="store_true")
    args = parser.parse_args()

    verbose = args.verbose

    if args.playbook is None:
        playbook = "check-w.yml"
    else:
        playbook = args.playbook

    if args.user is None:
        user = "ubuntu"
    else:
        user = args.user

    if verbose:
        print("verbose: ", verbose)
        print("playbook: ", playbook)
        print("user: ", user)

    log_file = "reports/report-" + date + ".log"
    hosts_file = open("hosts.txt", "r")
    report = open(log_file, 'w')

    disk_space_check = []
    for size in range(80, 101):
        disk_space_check.append(str(size) + "%")

    found_host_issue = []
    host_num = 0
    for host_line in hosts_file:
        if "[" in host_line:
            group = host_line
            if verbose:
                print("Group: ", group)
        elif host_line != "":
            host_num += 1
            print("### Host Num:", host_num)
            print("Host Details:", host_line.strip())
            host = host_line.split(" ")[0]
            print("Address:", host)
            host_one = open("ansible_host.txt", 'w')
            host_one.write("[default]\n")
            host_one.write(host + "\n")
            host_one.close()

            try:
                print("CMD: ansible-playbook", playbook, "-i", "ansible_host.txt", "-u", user, ssh_private_key)
                if ssh_private_key != "":
                    output = subprocess.check_output(['ansible-playbook', playbook, '-i', "ansible_host.txt", "-u", user, ssh_private_key])
                else:
                    output = subprocess.check_output(['ansible-playbook', playbook, '-i', "ansible_host.txt", "-u", user])
            except Exception as e:
                print("error running command", e)
                exit(1)
            report.write("Host Details: " + host_line)
            for line in output.decode("utf-8").split("\n"):
                if verbose:
                    print(line.strip())

                # Check disk space over threshold
                for disk_space in disk_space_check:
                    if disk_space in line and check_disk_name in line:
                        if verbose:
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
