#-----------------------Fleet Installation------------------------------
sudo ./elastic-agent install --fleet-server-es=https://server_ip:9200 \
 --fleet-server-es-ca=/etc/elasticsearch/certs/http_ca.crt --fleet-server-service-token=?? \
 --fleet-server-policy=fleet-server-policy


sudo ./elastic-agent install \
  --fleet-server-es=https://fleet_server_ip:9200 \
  --fleet-server-es-ca=/home/apgadm/elasticsearch-8.4.3/config/certs/http_ca.crt \
  --fleet-server-service-token=?? \
  --fleet-server-policy=fleet-server-policy


curl -f https://ip_or_domain:8220/api/status --insecure