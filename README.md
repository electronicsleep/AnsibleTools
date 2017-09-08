# Ansible Examples

#MacOS

brew install ansible

#Debian

apt-get install ansible

sudo vim /etc/ansible/hosts

ansible default -m ping -u ubuntu

ansible default -a "w" -u ubuntu

ansible default -a "ps -ef" -u ubuntu

# Get Facts

ansible default -m setup -u ubuntu

# Run Playbooks

ansible-playbook check-lamp.yml -u ubuntu

ansible-playbook check-os.yml -u ubuntu

ansible-playbook update-os.yml -u ubuntu

ansible-playbook build-nagios-client.yml -u ubuntu

# Resources

https://www.ansible.com

http://docs.ansible.com
