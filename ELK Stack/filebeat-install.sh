#--------------------Filebeat Installation--------------------

#on any system you want to monitor it using filebeat start installation on this server
curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.3.3-x86_64.rpm
sudo rpm -vi filebeat-8.3.3-x86_64.rpm
#or use 
sudo yum install filebeat


vi /etc/filebeat/filebeat.yml
#change these paramaters in filebeat input section if you want use for input log files
#type: log
#enabled: true
#paths:  -----the location of log files for example-------
#   - /opt/apigee/var/log/apigee-cassandra/*.log 
#if you want to send data to logstash not elk directly change the following parameters
#comment output.elasticsearch: and hosts
#Uncomment output.logstash: and hosts and assign it the public ip of logstash server  ["??"]


sudo systemctl start filebeat.service
sudo systemctl enable filebeat.service
sudo systemctl start filebeat.service 
sudo systemctl status filebeat.service 