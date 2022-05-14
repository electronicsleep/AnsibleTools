# Ansible Tools

Bootstrap tools/examples for Ansible infrastructure DevOps automation.
Shows some of the simple concepts and also includes some Python Boto3 examples.

Ansible and Python can be used together to get more power and control.

#### MacOS Install

```
brew install ansible python3
```

#### Debian Install

```
apt-get install ansible python3 python3-pip
```

#### Generate Inventory

```
pip3 install -r requirements.txt
python3 boto/get_inventory.py > hosts.txt
```

Update ansible.conf file if needed: `~/.ansible.conf`

Example:
```
[defaults]
host_key_checking = False
retry_files_enabled = False
private_key_file = ~/.ssh/example.pem
nocows=1

```

#### Host inventory file

Example using AnsiblePython:

```
python3 ansiblePython.py -p check-w.yml -v
python3 ansiblePython.py -p check-top.yml -v
python3 ansiblePython.py -p check-disk.yml -v
```

#### Ansible Commands

```
ansible default -i hosts.txt -m ping -u ubuntu
ansible default -i hosts.txt -a "w" -u ubuntu
ansible default -i hosts.txt -a "ps -ef" -u ubuntu
ansible default -i hosts.txt -a "netstat -ta" -u ubuntu
```


#### Get Facts

```
ansible default -m setup -u ubuntu
```

#### Simple Playbooks (single file)

```
ansible-playbook -i hosts.txt check-user-load.yml -u ubuntu
```

#### Run Role Playbooks (roles directory)

```
ansible-playbook -i hosts.txt check-os.yml -u ubuntu
ansible-playbook -i hosts.txt check-lamp.yml -u ubuntu
# ansible-playbook -i hosts.txt update-os.yml -u ubuntu
# ansible-playbook -i hosts.txt build-base-os.yml -u ubuntu
# ansible-playbook -i hosts.txt build-nagios-client.yml -u ubuntu
```

#### Best Practices

Use --check

Use --syntax-check

Use --list-hosts

#### Troubleshooting

Make sure Python is installed on target hosts


#### Resources

https://www.ansible.com

http://docs.ansible.com
