### Build the Docker Image:
Build the Docker image containing your Gatling script and dependencies.

```bash
docker build -t gatling-test .
```

### Push Docker Image to Registry:
If you're using a private container registry, push the Docker image to the registry.

```bash
docker tag gatling-test 314201/gatling-test
docker push 314201/gatling-test
```

### Apply the Job YAML:
Apply the Kubernetes Job YAML to create the Job in your Kubernetes cluster.
```bash
kubectl apply -f gatling-job.yaml
```

### Delete the Job if it already exists before apply:
Delete the Job present in your Kubernetes cluster.
```bash
kubectl delete -f gatling-job.yaml
```
