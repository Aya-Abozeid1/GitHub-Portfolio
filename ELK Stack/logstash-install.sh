#--------------Logstash installation---------------

yum install java-1.8.0-openjdk 

sudo rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

cd /etc/yum.repos.d/
vi logstash.repo
#add this content to the above file

[logstash-8.x]
name=Elastic repository for 8.x packages
baseurl=https://artifacts.elastic.co/packages/8.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md

sudo yum install logstash

vi /etc/logstash/conf.d/logstash-sample.conf
# and add the next content
input {
    tcp {
        port => 5044
        type => syslog
    }
}
#or input could be this if it is from beats
input {
  beats {
    port => 5044
  }
}
filter {
    mutate {
        gsub => [
            "message", "[\u0000]", ""
        ]
        remove_field => ["timestamp", "host", "facility_label", "severity_label", "severity", "facility", "priority"]
    }
    grok {
        match => {"message" => "<%{NUMBER:priority_index}>%{DATESTAMP_OTHER:apigeeTimestamp}%{LOGLEVEL}: %{GREEDYDATA:apigeeMessage}"}
        remove_field => ["message"]
    }
    json {
        source => "apigeeMessage"
        target => "message"
        remove_field => ["apigeeMessage"]
    }
}
output {
    elasticsearch {
        # Your node IP addresses from the Instaclustr Console
        hosts => ["??"]

        user => "elastic"
        password => "??"
        ssl_certificate_verification => false
        # The name of the Index
        index => "apigee-%{+YYYY.MM.dd}"
    }
}

#exit and start the service

sudo systemctl start logstash.service
sudo systemctl enable logstash.service
sudo systemctl start logstash.service
sudo systemctl status logstash.service


#to test logstash
cd /usr/share/logstash
bin/logstash -e 'input { stdin { } } output { stdout {} }'
#OR
sudo -u logstash /usr/share/logstash/bin/logstash --path.settings /etc/logstash -t
/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/logstash-sample.conf --debug
