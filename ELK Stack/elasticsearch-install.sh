--------------------ElasticSearch Installation RHEL-----------------------
#open port 9200, 9300, 5601,8080,80,443

#https://docs.datastax.com/en/jdk-install/doc/jdk-install/installOpenJdkRHEL.html
yum install java-1.8.0-openjdk 

rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
cd /etc/yum.repos.d/
vi elasticsearch.repo 
#add this content to the above file

[elasticsearch]
name=Elasticsearch repository for 8.x packages
baseurl=https://artifacts.elastic.co/packages/8.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=0
autorefresh=1
type=rpm-md


sudo yum install --enablerepo=elasticsearch elasticsearch
#after Installation save the security configuration output aside


#------for multinode cluster---------
#before you start the new node
#run the next command on the master node
/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s node 
#run the next command on the new node 
/usr/share/elasticsearch/bin/elasticsearch-reconfigure-node --enrollment-token <output from above command>
#after that edit /etc/elasticsearch/elasticsearch.yml
#uncomment cluster name and assign it the same name as master
#uncomment node name and assign it a unique value
#uncomment network.host and assign it 0.0.0.0
#uncommment http.port
#uncomment transport.port ----> on master node


sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable elasticsearch.service
sudo systemctl start elasticsearch.service


#for checking status
curl --cacert /etc/elasticsearch/certs/http_ca.crt -u elastic https://localhost:9200 
curl -XGET 'http://localhost:9200/?pretty'
curl -X GET "https://localhost:9200/_cluster/health?wait_for_status=yellow&timeout=50s&pretty" --key certificates/elasticsearch-ca.pem  -k -u elastic
curl --insecure https://localhost:9200/_cluster/health?pretty -u elastic
curl --insecure https://localhost:9200/_nodes/stats/process?filter_path=**.max_file_descriptors -u elastic


#vi /etc/sysconfig/elasticsearch
# uncomment #ES_JAVA_HOME and assign it /usr/share/elasticsearch/jdk and uncomment ES_HOME

tail -f -n 100 /var/log/elasticsearch/my-application.log 
tail -f -n 20 /var/log/logstash/logstash-plain.log 
vi /var/log/elasticsearch/my-cluster.log

#to remove elastic
yum remove elasticsearch
sudo rm -rf /etc/elasticsearch
sudo rm -rf /var/lib/elasticsearch