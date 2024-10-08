# Apigee API Deployment Automation

This repository contains automation scripts for deploying Apigee APIs using a Jenkins pipeline. The pipeline includes a stage for scanning the API code with SonarQube before proceeding with the build and deployment processes.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Jenkins Pipeline Configuration](#jenkins-pipeline-configuration)
- [SonarQube Configuration](#sonarqube-configuration)
- [Deployment Process](#deployment-process)


## Overview
This automation script provides a continuous integration and deployment (CI/CD) solution for Apigee APIs. It ensures that the code quality is maintained by integrating SonarQube for static code analysis, followed by the building and deployment of APIs into the Apigee environment.

## Prerequisites
Before using this automation script, ensure you have the following set up:
- **Jenkins**: An instance of Jenkins must be installed and running.
- **SonarQube**: A SonarQube server must be set up for code scanning.
- **Apigee Account**: Access to an Apigee organization where the APIs will be deployed.
- **Git**: Ensure Git is installed for source code management.
- **API Code**: The API source code should be available in a Git repository.

## Jenkins Pipeline Configuration
The Jenkins pipeline is defined in the `Jenkinsfile`. It includes the following stages:
- **Note**: Update setenv.sh with the correct values of Apigee environment variables
1. **SonarQube Scan**: Invokes the SonarQube scan to analyze the code quality.
2. **Build**: Executes the build script (`env_conf_setup.sh`) to compile the API.
3. **Deploy**: Runs the deployment script (`deploy_all.sh`) to deploy the API to the specified Apigee environment.

## SonarQube Configuration
## To configure SonarQube:

Ensure that your SonarQube server is running and accessible.
Configure the necessary credentials and project settings in the SonarQube dashboard.
Update the Jenkinsfile script with the correct SonarQube project key and server URL.

## Deployment Process
## The deployment process includes:

- Code Scanning: The API code is scanned for vulnerabilities and code quality issues using SonarQube.
- Building: The API is built using the build script.
- Deploying: The built API is deployed to the specified Apigee environment using the deployment script.