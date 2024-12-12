# Ansible Tools

Bootstrap tools/examples for Ansible infrastructure DevOps automation.
Shows some of the simple concepts and also includes some Python Boto3 examples.
Ansible and Python can be used together for additional host logging and control.

#### MacOS Install

```
brew install ansible python3
```

#### Ubuntu/Debian Install

```
apt-get install ansible python3 python3-pip
```

#### Generate Inventory

```
brew install virtualenv
virtualenv tempEnv
source tempEnv/bin/activate
pip3 install -r requirements.txt
python3 src/boto/get_inventory.py > hosts.txt
```

Update ansible config file as needed: `~/.ansible.cfg`

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
Shows host info at Runtime with name from Boto3 command

Example
```
################################################################################
Host Details: xx.xx.xx.xx # i-12345 NAME_UL running Host: 1
IPAddress: xx.xx.xx.xx
################################################################################
```

Command
```
python3 src/ansiblePython.py -p check-w.yml -v
python3 src/ansiblePython.py -p check-top.yml -v
python3 src/ansiblePython.py -p check-disk.yml -v
```

#### Run Playbooks (roles directory)

```
ansible-playbook -i hosts.txt src/check-os.yml -u ubuntu
ansible-playbook -i hosts.txt src/check-lamp.yml -u ubuntu
```

#### Ansible Commands

```
ansible default -i hosts.txt -m ping -u ubuntu
ansible default -i hosts.txt -a "w" -u ubuntu
ansible default -i hosts.txt -a "ps -ef" -u ubuntu
ansible default -i hosts.txt -a "netstat -ta" -u ubuntu
```

#### Simple Playbooks (single file)

```
ansible-playbook -i hosts.txt check-user-load.yml -u ubuntu
```

#### Get Facts

```
ansible default -m setup -u ubuntu
```

#### Best Practices

Use --check
Use --syntax-check
Use --list-hosts

#### Troubleshooting

Ensure Python is installed on target hosts

#### Resources

https://www.ansible.com

http://docs.ansible.com
