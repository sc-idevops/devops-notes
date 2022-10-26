pods_with_requests=""
pods_without_requests=""

for namespace in `kubectl get namespaces | grep -v NAME | cut -d ' ' -f 1` ; do
  for pod in `kubectl get pods -n $namespace | grep -v NAME | cut -d ' ' -f 1` ; do
        requests_check=`kubectl get pods $pod -n $namespace -o yaml | grep requests`
        if [ ! -z "$requests_check" ]; then
           pods_with_requests="$pods_with_requests\n$pod,$namespace"
        else
           pods_without_requests="$pods_without_requests\n$pod,$namespace"
        fi
  done
done

echo "Pods With request Checks"
echo $pods_with_requests

echo ""
echo ""
echo "========="
echo ""
echo ""

echo "Pods Without request Checks"
echo $pods_without_requests
