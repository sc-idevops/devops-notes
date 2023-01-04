# flask-ansible-task
Ansible-Playbook to deploy simple nginx site
You'll have to bring your own pem file :P

## Process:
- terraform
  - terraform init
  - terraform plan/apply
  - get public IP output

- ansible:
  - put public IP into the .hosts file
  - execute playbook: `ansible-playbook -i .hosts deploy.yml`
