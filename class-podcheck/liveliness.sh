pods_with_liveliness_probes=""
pods_without_liveliness_probes=""

for namespace in `kubectl get namespaces | grep -v NAME | cut -d ' ' -f 1` ; do
  for pod in `kubectl get pods -n $namespace | grep -v NAME | cut -d ' ' -f 1` ; do
        liveliness_check=`kubectl get pods $pod -n $namespace -o yaml | grep livenessProbe`
        if [ ! -z "$liveliness_check" ]; then
           pods_with_liveliness_probes="$pods_with_liveliness_probes\n$pod,$namespace"
        else
           pods_without_liveliness_probes="$pods_without_liveliness_probes\n$pod,$namespace"
        fi
  done
done

echo "Pods With Liveliness Checks"
echo $pods_with_liveliness_probes

echo ""
echo ""
echo "========="
echo ""
echo ""

echo "Pods Without Liveliness Checks"
echo $pods_without_liveliness_probes
