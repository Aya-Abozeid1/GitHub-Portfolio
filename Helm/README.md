# Helm Chart for Frontend, Backend Apps, and Cron Job

## Overview

This repository contains a Helm chart that simplifies the deployment of frontend and backend applications, along with a cron job. The chart includes templates for Kubernetes resources such as Deployments, Services, Ingress, Service Accounts, and Volumes. These components can be customized through the provided `values.yaml` file to suit various use cases.

## Features

- **Frontend and Backend Deployment**: Easily deploy your frontend and backend applications using Helm.
- **Cron Job Support**: Includes a Kubernetes CronJob for scheduled tasks.
- **Service Creation**: Automatically creates Kubernetes Services to expose your frontend and backend apps.
- **Ingress Support**: Set up Ingress to manage external access to your apps.
- **Service Account**: Configure a ServiceAccount for managing Kubernetes permissions.
- **Volume Mounts**: Persistent Volumes can be configured to store and manage app data.

## Prerequisites

Before deploying this Helm chart, ensure you have the following:

1. **Kubernetes Cluster**: A running Kubernetes cluster (either locally via Minikube or on cloud platforms like AKS, GKE, etc.).
2. **Helm**: Ensure Helm is installed in your local environment.
   - [Helm installation guide](https://helm.sh/docs/intro/install/)


## Chart Structure
## The Helm chart contains the following main components:

**Deployment**:
- deployment.yaml: Deployment resource for the frontend application.
                    Deployment resource for the backend application.
                    Kubernetes CronJob for scheduled tasks.
**Service**:
- service.yaml: Service for exposing the frontend application.
                       Service for exposing the backend application.
**Ingress**:
- ingress.yaml: Ingress resource to route external traffic to the apps.

**Service Account**:
- serviceaccount.yaml: Service account for managing access control within the Kubernetes cluster.

**Volumes**:
- volumes.yaml: Persistent volume claims for storing data.

## Customization
- You can customize the following components through the values.yaml file:

**Frontend & Backend Configuration**:
- Set container images, environment variables, and resource limits for both applications.

**Cron Job**:
- Define the schedule and job details.

**Service and Ingress**:
- Configure ports, service types (ClusterIP, NodePort, etc.), and ingress hostname/rules.

**Volumes**:
- Define volume claims, storage classes, and mount points.
