# Ansible Examples

Bootstrap examples for Ansible infrastructure automation for training others in Ansible. 

Repo shows some of the simple concepts and also includes some Python Boto3 examples as well.

Normally I use Ansible and Python together to get more power and control with parsing and flow.

Examples use python3 but older versions should be supported

#### MacOS Install

brew install ansible
brew install python3

#### Debian Install

apt-get install ansible
apt-get install python3

#### Generate Inventory

pip install -r requirements.txt

python boto/get_inventory.py

sudo vim /etc/ansible/hosts

#### Host inventory file

Example using Ansible and Python together

python ansiblePython.py

python ansiblePython.py -p check-top.yml

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
