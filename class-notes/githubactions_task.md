# Steps to Create Github Action from Vaas Repo

Example will be based on **K8S:DEPLOYMENT:JUPYTERHUB**
#### Steps
- Step 0: Clone vaas repo & idevops-git-actions
- Step 1: Create folder for tech_name and paste dockerfile, deployment.yaml.template, and action.yml
- Step 2: Copy Contents of yaml.template and paste into readme. delete everything except the Grant syntax variables (things surrounded by -=thing=-)
- Step 3: prettify the variables with a description, defaults, and if it's required in action.yml
- Step 4: Begin setting up runs using composite actions.
    - use our docker build and push action
    - anchore image scan
    - 