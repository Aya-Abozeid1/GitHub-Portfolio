# Apigee On-Premises Installation Scripts

## Overview
This repository contains a set of scripts to simplify the installation of Apigee on-premises. Each script is designed to install a specific Apigee component. The scripts automate the setup process, reducing manual intervention and ensuring a smooth installation.

### Apigee Components Installed by These Scripts:
1. **Management Server (MS)**
2. **Router**
3. **Message Processor (MP)**
4. **PostgreSQL (Analytics & KMS Databases)**
5. **Qpid (Messaging Service)**

## Scripts Overview

| Script Name               | Component Installed                       | Description                                       |
| ------------------------- | ----------------------------------------- | ------------------------------------------------- |
| `install-management-server.sh` | Management Server (MS)                    | Installs and configures the Apigee Management Server. |
| `install-router.sh`           | Router                                    | Installs and configures the Apigee Router component.  |
| `install-message-processor.sh`| Message Processor (MP)                     | Installs the Message Processor for Apigee.           |
| `install-postgresql.sh`       | PostgreSQL (Analytics & KMS Databases)     | Installs PostgreSQL for Apigee analytics and KMS.    |
| `install-qpid.sh`             | Qpid (Messaging Service)                   | Installs the Qpid messaging service for Apigee.       |

## Prerequisites
Before running any of the scripts, ensure that the following prerequisites are met:

- **Operating System**: CentOS/RedHat or similar Linux distribution
- **Root or Sudo Access**: You need root or sudo privileges to run the scripts.
- **Internet Access**: Ensure the machine has access to the internet for downloading dependencies.
- **Apigee License**: A valid Apigee license for on-prem installation.

### Pre-Installation Steps
1. Ensure you have a **fresh, minimal installation** of the supported OS.
2. Configure **firewalls** to allow traffic between the Apigee components.
3. Set up **hostname resolution** for each component (e.g., via `/etc/hosts` or DNS).
4. Install **Java** and set the `JAVA_HOME` environment variable.
   
## Installation Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/apigee-onprem-install-scripts.git
   cd apigee-onprem-install-scripts
