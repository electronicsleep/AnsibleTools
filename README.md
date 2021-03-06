# Ansible Tools

Bootstrap tools/examples for Ansible infrastructure DevOps automation.
Shows some of the simple concepts and also includes some Python Boto3 examples.

Ansible and Python can be used together to get more power and control.

Examples use Python3 but older versions should be supported.

#### MacOS Install

brew install ansible python3

#### Debian Install

apt-get install ansible python3 python3-pip

#### Generate Inventory

pip install -r requirements.txt

python boto/get_inventory.py > hosts.txt

Update any key files in ~/.ansible.conf see example

#### Host inventory file

Example using Ansible and Python together

python ansiblePython.py -p check-w.yml -v

python ansiblePython.py -p check-top.yml -v

python ansiblePython.py -p check-disk.yml -v

#### Ansible Commands

ansible default -m ping -u ubuntu

ansible default -a "w" -u ubuntu

ansible default -a "ps -ef" -u ubuntu

ansible default -a "netstat -ta" -u ubuntu

#### Best Practices

Use --check

Use --syntax-check

Use --list-hosts

#### Get Facts

ansible default -m setup -u ubuntu

#### Simple Playbooks (single file)

ansible-playbook check-user-load.yml -u ubuntu

#### Run Role Playbooks (roles directory)

ansible-playbook check-lamp.yml -u ubuntu

ansible-playbook check-os.yml -u ubuntu

ansible-playbook update-os.yml -u ubuntu

ansible-playbook build-base-os.yml -u ubuntu

ansible-playbook build-nagios-client.yml -u ubuntu

#### Resources

https://www.ansible.com

http://docs.ansible.com
