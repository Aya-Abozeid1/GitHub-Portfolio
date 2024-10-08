#!/usr/bin/env python3
import sys
import getopt
import http.client
import json
import requests
from requests.structures import CaseInsensitiveDict
from requests.auth import HTTPBasicAuth

ApigeeHost = None
User = None
UserPW = None
Organization = None
Environment = None
scripts_path= None



Options = 'h:u:e:o:p:d:'
opts = getopt.getopt(sys.argv[1:], Options)[0]
for o in opts:
    if o[0] == '-o':
        Organization = o[1]
    elif o[0] == '-h':
        ApigeeHost = o[1]
    elif o[0] == '-e':
        Environment = o[1]
    elif o[0] == '-u':
        User = o[1]
    elif o[0] == '-p':
        UserPW= o[1]
    elif o[0] == '-d':
        scripts_path= o[1]        


url =  ApigeeHost+"/v1/organizations/"+Organization+"/environments/"+Environment
auth = HTTPBasicAuth(User,UserPW)

def create_kvm():
    requestUrl=url+"/keyvaluemaps/"
    kvm_file = scripts_path + "kvm.json"
    print(kvm_file)
    try:
        f = open(kvm_file)
        try: 
            kvm=json.load(f)
            for kvm in kvm['kvm']:
                resp = requests.post(requestUrl, json=kvm, auth=auth)
                print((resp.text))
        except json.decoder.JSONDecodeError: print("kvm.json has invalid syntax error")
    except FileNotFoundError: print("kvm.json is not found")    
    


def create_target_server():
    requestUrl = url+"/targetservers/"
    target_server_file = scripts_path + "target_servers.json"
    try:
        f = open(target_server_file)
        try:
            target_server=json.load(f)
            for target_server in target_server['target_servers']:
                resp = requests.post(requestUrl, json=target_server, auth=auth) 
                print((resp.text))
        except json.decoder.JSONDecodeError: print("target_servers.json has invalid syntax error")
    except FileNotFoundError: print("target_servers.json is not found")            
     


def create_caches():
    requestUrl = url+"/caches"
    caches_file = scripts_path + "caches.json"
    try:
        f = open(caches_file)
        try:
            caches=json.load(f)
            for cache in caches['caches']:
                resp = requests.post(requestUrl, json=cache, auth=auth)
                print((resp.text))
        except json.decoder.JSONDecodeError: print("caches.json has invalid syntax error")   
    except FileNotFoundError: print("caches.json is not found")    



if __name__ == '__main__':
    create_kvm()
    create_target_server()
    create_caches()

