#!/bin/bash

source ./setup/setenv.sh

echo Using $username in $env Environment of $org Organization.


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
  echo "Verfied! Proceeding with Environment Configuration Setup."
fi;

#run env configuration setup script
chmod 755 ./tools/env_confguration_setup.py
./tools/env_confguration_setup.py -h $url -u $username -p $password -o $org -e $env -d "./env-configuration/"


