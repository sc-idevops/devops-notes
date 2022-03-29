# Kubernetes
## Problems?
If a pod is crashing, check for:
* Events by describing the pod
* Logs

## Commands
kubectl logs $POD_NAME -n $NAMESPACE
    * Shows log of namespace
kubctl get pods --all-namespaces
    * Shows all namespaces
    * Add -w to watch it for changes
kubectl describe pods -n $NAMESPACE $PODNAME
    * describes namespace/conditions/volumes/Events
kubectl exec -n $NAMESPACE -it $PODNAME -- bash
    * executes into namespace. what happens after -- indicates what to execute
kubectl delete namespace amazonlinux
    * deletes and cleans entire namespace
    
## Kubernetes Spec Minimum Requirements:
* Containers: Image Name


Since containers aren't changed unless you include an attached volume, everything you do will be deleted when the pod dies.

In a deployment file, our variables that get replaced by a python script are put in grant format surrounded by `-==-`'s

Services are used in the yaml file to facilitate network communications and over what ports. 

## Rollouts
`kubectl rollout status`
this command checks the status of your pod rolling out.
your new pod has a ready state
* 0/1 means not ready yet
* 1/1 means its ready

your pod will wait until it sees 1/1 ready state. 
if it times out, your deployment could not be validated

## Config Maps

if your tech requires a config file you can have the deployment template include it for you instead of copying it in with your docker file command.

a file will be mounted where you specify, and then you include what the contents of the file should be.

example config map: from (https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap)
```
apiVersion: v1
kind: ConfigMap
metadata:
  creationTimestamp: 2016-02-18T18:52:05Z
  name: game-config
  namespace: default
  resourceVersion: "516"
  uid: b4952dc3-d670-11e5-8cd0-68f728db1985
data:
  game.properties: |
    enemies=aliens
    lives=3
    enemies.cheat=true
    enemies.cheat.level=noGoodRotten
    secret.code.passphrase=UUDDLRLRBABAS
    secret.code.allowed=true
    secret.code.lives=30    
  ui.properties: |
    color.good=purple
    color.bad=yellow
    allow.textmode=true
    how.nice.to.look=fairlyNice    
```

We're also going to need volume mounts under the container spec.
https://github.com/iDevOps-io/vaas/blob/d40453649b57d58e700456ac7e7c8c44f277f866/manifests/haproxy/deployment.yaml.template
