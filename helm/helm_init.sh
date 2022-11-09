CHART_REPO_NAME=bitnami-redis
CHART_REPO_URL=https://charts.bitnami.com/bitnami
CHART_NAME=redis
NAMESPACE=redis-card
HELM_INSTALL_NAME=redis

echo "add helm repo & install"
helm repo add ${CHART_REPO_NAME} ${CHART_REPO_URL}
helm install ${HELM_INSTALL_NAME} ${CHART_REPO_NAME}/${CHART_NAME} -n ${NAMESPACE} --create-namespace -f values.yaml

echo "install python dependencies"
pip3 install redis

echo "run python test program"
python3 helm.py

echo "remember to delete your namespace"
#kubectl delete namespace ${NAMESPACE}