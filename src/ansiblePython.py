#!/usr/bin/env python
# Author: https://github.com/electronicsleep
# Purpose: Using Ansible and Python for more control
# Released under the BSD license

import subprocess
import argparse
import datetime
from termcolor import colored

date = datetime.datetime.now().strftime("%Y%m%d-%H%M")
print(f"report date: {date}")
check_disk_name = "/dev/xvda1"
check_load_avg = "load average:"
root_dir = ""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--playbook", help="playbook to run", required=False)
    parser.add_argument("-u", "--user", help="user for host", required=False)
    parser.add_argument("-v", "--verbose", help="show more output", required=False, action="store_true")
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
        print(f"verbose: {verbose}")
        print(f"playbook: {playbook}")
        print(f"user: {user}")

    log_file = root_dir + "src/reports/report-" + date + ".log"
    hosts_file = open(root_dir + "hosts.txt", "r")
    report = open(log_file, 'w')

    disk_space_check = []
    for size in range(95, 101):
        disk_space_check.append(str(size) + "%")

    found_host_issue = []
    host_num = 0
    for host_line in hosts_file:
        host_num += 1
        print("#" * 80)
        print_info("Host Details: " + host_line.strip() + " Host: " + str(host_num))
        host = host_line.split(" ")[0]
        print("#" * 80)
        host_one = open(root_dir + "ansible_host.txt", 'w')
        host_one.write("[default]\n")
        host_one.write(host + "\n")
        host_one.close()
        print("Playbook: " + root_dir + "src/" + playbook)
        try:
            output = subprocess.check_output(['ansible-playbook', root_dir + "src/" + playbook, '-i', root_dir + "ansible_host.txt", "-u", user]) # noqa
        except subprocess.CalledProcessError as e:
            print("Error:", e)
            exit(1)
        report.write("Host Details: " + host_line)
        for line in output.decode("utf-8").split("\n"):
            if verbose:
                print(line.strip())

            if playbook == "check-w.yml" or playbook == "check-top.yml":
                check_disk_parse(found_host_issue, host_line, line, check_load_avg)

            if playbook == "check-disk.yml":
                check_disk_parse(disk_space_check, found_host_issue, host_line, line)

            report.write(f"{line}\n")

    if len(found_host_issue) == 0:
        print_info("No issues found")
    for item in found_host_issue:
        print(f"Playbook: {playbook}")
        print_error(f"HOST ISSUE: {item}")
        report.write(f"HOST ISSUE: {host}: {item}\n")
    print(f"Wrote Log: {log_file}")
    report.close()


def check_disk_parse(disk_space_check, found_host_issue, host_line, line):
    """Check disk space over threshold"""
    for disk_space in disk_space_check:
        if disk_space in line and check_disk_name in line:
            print_error(f"Found disk over threshold: {disk_space}")
            found_host_issue.append(host_line + " -  " + line)


def check_load_threshhold(found_host_issue, host_line, line, check_load_avg):
    """Check load over threshold"""
    if check_load_avg in line:
        check_load_line = line.split()
        check_load_avg_line = check_load_line[-3:]
        load_avg_1m = check_load_avg_line[0].split(".")
        load_avg_1m = int(load_avg_1m[0])
        print("LOAD:", load_avg_1m)
        if load_avg_1m > 0:
            print_error(f"Found load over 0: {check_load_avg}")
            found_host_issue.append(host_line + " -  " + line)


def print_error(message):
    print(colored(message, 'red'))


def print_info(message):
    print(colored(message, 'yellow'))


if __name__ == '__main__':
    main()
