# Ansible
Ansible uses YAML files to execute commands on machines automatically.

example file
```
---
- hosts: all
  become: yes
  tasks:
    - name: Update apt cache & install curl
    apt:
        name: curl
        update_cache: yes
```
This will install curl on all managed computers. These files are called playbooks (isn't that cute)

Ansible looks at a hosts file to know what ssh server(s) to contact and run the commands on.

`ansible-playbook -i hosts_file playbook_file.yaml` executes a playbook file. 

Note: If you wanted you could execute a playbook locally too!

Ansible enforces configuration management: forcing a desired state on the systems


