pods_with_readiness_probes=""
pods_without_readiness_probes=""

for namespace in `kubectl get namespaces | grep -v NAME | cut -d ' ' -f 1` ; do
  for pod in `kubectl get pods -n $namespace | grep -v NAME | cut -d ' ' -f 1` ; do
        readiness_check=`kubectl get pods $pod -n $namespace -o yaml | grep readinessProbe`
        if [ ! -z "$readiness_check" ]; then
           pods_with_readiness_probes="$pods_with_liveliness_probes\n$pod,$namespace"
        else
           pods_without_readiness_probes="$pods_without_liveliness_probes\n$pod,$namespace"
        fi
  done
done

echo "Pods With readiness Checks"
echo $pods_with_readiness_probes

echo ""
echo ""
echo "========="
echo ""
echo ""

echo "Pods Without readiness Checks"
echo $pods_without_readiness_probes
