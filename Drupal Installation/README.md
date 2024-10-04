# Drupal Installation Guide

This repository contains configuration files and instructions for deploying **Drupal** using two different methods:

1. **Docker and Docker Compose**: A quick way to set up Drupal locally or on a server using Docker.
2. **Kubernetes**: For deploying Drupal in a more scalable and production-ready environment using Kubernetes.

## Prerequisites

- **For Docker and Docker Compose**:
  - Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
  - Docker Compose installed ([Install Docker Compose](https://docs.docker.com/compose/install/))

- **For Kubernetes**:
  - A running Kubernetes cluster ([Minikube](https://minikube.sigs.k8s.io/docs/start/) for local setup)
  - `kubectl` installed ([Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/))
  - Helm (optional for PostgreSQL) ([Install Helm](https://helm.sh/docs/intro/install/))
  - Persistent storage configured (e.g., NFS, cloud storage, or local volumes)

