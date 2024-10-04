-------------------------kibana Installation---------------------------------

rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
cd /etc/yum.repos.d/
vi kibana.repo
#add this content to the above file

[kibana-8.x]
name=Kibana repository for 8.x packages
baseurl=https://artifacts.elastic.co/packages/8.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md

sudo yum install kibana 

#to activate rules and connectors
/usr/share/kibana/bin/kibana-encryption-keys generate
vim /etc/kibana/kibana.yml
#and add thise content that was generated from above command
#xpack.encryptedSavedObjects.encryptionKey: ???
#xpack.reporting.encryptionKey: ???
#xpack.security.encryptionKey: ???

/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana

sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable kibana.service
sudo systemctl start kibana.service
sudo /bin/systemctl enable kibana.service

#to check status 
journalctl -u kibana.service

#to check the page responses and it should output the html content
curl http://localhost:5601/?code=142923

cd /etc/kibana

vi kibana.yml #uncomment server.port and uncomment server.host and replace localhost with 0.0.0.0

#-------optional------
sudo setenforce 0
vi /etc/sysconfig/selinux
systemctl stop firewalld
#---------------------
sudo systemctl restart kibana.service

#for verification code you can find it using this command
cd /usr/share/kibana/bin
./kibana-verification-code    #this will ouput the code
 nohup ./bin/kibana &
