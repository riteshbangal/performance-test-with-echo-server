# Echo Server in Kubernetes

This repository contains a basic echo server implemented in Python, deployed on Kubernetes. The echo server listens on a specified port and returns any received data as a response.

## Docker Image

The server is packaged into a Docker image, using a multi-stage build to keep the image size minimal. It uses the `busybox` base image to achieve a smaller footprint.

### Build and Push Docker Image

To build the Docker image, use the following commands:

```bash
docker build -t 314201/echo-server:latest .
```

### Push the image to Docker Hub:

```bash
docker push 314201/echo-server:latest
```
Make sure to log in to your Docker Hub account using docker login before pushing.

## Kubernetes Deployment
The Kubernetes deployment consists of a Deployment and a Service. The echo server is deployed with two replicas to ensure availability.

### Apply Deployment and Service
To deploy the echo server on your Kubernetes cluster, apply the following YAML files:

```bash
kubectl apply -f echo-server-deployment.yaml
kubectl apply -f echo-server-service.yaml
```

The service is exposed externally on port 80.

### Use Port Forwarding for Local Testing:
If you still need to test the service locally, you can use kubectl port-forward to forward a local port to the LoadBalancer service:

```bash
kubectl port-forward service/echo-server-service 8080:80
```

### Test the Echo Server
Once the deployment is successful, you can test the echo server by sending a request:

```bash
while true; do  curl localhost:8080; echo "Success"; sleep 1; done
while true; do  curl http://localhost:8080/perf_test; echo "Success"; sleep 1; done
```