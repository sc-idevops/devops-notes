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
TODO: rip that from his template haproxy on github

