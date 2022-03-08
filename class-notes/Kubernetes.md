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
