#!/bin/bash


sudo yum install curl wget -y
# Prerequisite: Enable EPEL repo
yum install wget
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
sudo rpm -ivh epel-release-latest-7.noarch.rpm
# Download the Edge bootstrap
sudo yum install curl
curl https://software.apigee.com/bootstrap_4.51.00.sh -o /tmp/bootstrap_4.51.00.sh


cp -R /tmp/apigee-4.18.05.tar.gz  /u01/apigee/software

# Stop SELinux 
sudo setenforce 0


# install Edge apigee-setup utility
sudo yum install yum-utils -y
sudo yum install yum-plugin-priorities -y

# do a link to the apigee installation /opt/apigee
groupadd -r apigee > useradd -r -g apigee -d /opt/apigee -s /sbin/nologin -c "Apigee platform user" apigee
sudo ln -Ts /u01/apigee /opt/apigee
sudo chown -h apigee:apigee /u01/apigee /opt/apigee

#  of the software and the confige file
/u01/apigee/software

tar -xzf apigee-4.51.00.tar.gz

# Install the Edge apigee-service utility and dependencies
sudo bash /u01/apigee/software/repos/bootstrap_4.51.00.sh apigeeprotocol="file://" apigeerepobasepath=/u01/apigee/software/repos

# Use apigee-service to install the apigee-setup utility
/opt/apigee/apigee-service/bin/apigee-service apigee-setup install

# fix java 
export _JAVA_OPTIONS="-Dcom.sun.jndi.rmiURLParsing=legacy"

#Install Analytics
/opt/apigee/apigee-setup/bin/setup.sh -p sax -f /u01/apigee/software/configFile


/opt/apigee/apigee-service/bin/apigee-all enable_autostart