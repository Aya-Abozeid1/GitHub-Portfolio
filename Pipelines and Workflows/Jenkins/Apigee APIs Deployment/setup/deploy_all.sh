#!/bin/bash

echo "Current Dir $(pwd)"
source ./setup/setenv.sh

echo This script deploys all sample API proxies under ./sample-proxies to your organization on the Apigee API Platform.

echo Be sure to populate values in setenv.sh in this directory before running this script.

echo Using $username in $org.

echo "Enter your password for the Apigee Enterprise organization $org, followed by [ENTER]:"

#read -s password
password=$pass

echo Verifying credentials...

response=`curl -s -o /dev/null -I -w "%{http_code}" $url/v1/organizations/$org -u $username:$password`

if [ $response -eq 401 ]
then
  echo "Authentication failed!"
  echo "Please re-run the script using the right username/password."
  exit
elif [ $response -eq 403 ]
then
  echo Organization $org is invalid!
  echo Please re-run the script using the right org.
  exit
else
  echo "Verfied! Proceeding with deployment."
fi;

echo Deploying all samples to $env using $username and $org

echo Creating caches

#curl -X POST -H "Content-type:text/xml" -d @../sample-proxies/outbound-oauth/oauth-token-cache.xml $url/v1/o/$org/environments/$env/caches -u $username:$password

#curl -X POST -H "Content-type:text/xml" -d @../sample-proxies/pagination/paginationCache.xml $url/v1/o/$org/environments/$env/caches -u $username:$password


cd ./proxies/
for proxydir in *; do
    if [ -d "${proxydir}" ]; then
        chmod 755 /opt/app/jenkins/workspace/ApiGee/Tawal_Pipeline/tools/deploy.py
        /opt/app/jenkins/workspace/ApiGee/Tawal_Pipeline/tools/deploy.py -n $proxydir -u $username:$password -o $org -e $env -p / -d $proxydir -h $url
    fi
done

cd /opt/app/jenkins/workspace/ApiGee/Tawal_Pipeline/setup/

echo "Deployment complete. Sample API proxies are deployed to the $env environment in the organization $org"

echo "Login to enterprise.apigee.com to view and interact with the sample API proxies"

echo "To invoke the samples, run invoke.sh found in each sample's directory in this distribution."

