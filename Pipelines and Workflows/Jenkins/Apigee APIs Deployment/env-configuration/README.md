### _________________________________Key Value Map___________________________________________

To create KVM, put all of your KVMs and their entries in one array of json objects structure 
and the array must be called "kvm" as shown below

{"kvm":[
    {
        "name": "kvm1",
        "encrypted": "false",
        "entry": [
            {
                "name": "key1",
                "value": "value1"
            },
            {
                "name": "key2",
                "value": "value2"
            }
        ]
    }
,

    {
        "name": "kvm2",
        "encrypted": "true",
        "entry": [
            {
                "name": "key3",
                "value": "value3"
            },
            {
                "name": "key4",
                "value": "value4"
            }
        ]
    }
]
}


### _________________________________Target Server___________________________________________


To create target server, put all of your target servers and their values in one array of json objects structure 
and the array must be called "target_servers" as shown below

{
    "target_servers": [
        {
            "host": "target_server_host",
            "isEnabled": true,
            "name": "target-server1",
            "port": 80
        },
        {
            "host": "target_server_host",
            "isEnabled": false,
            "name": "target-server2",
            "port": 443
        }
    ]
}


### _________________________________ Caches ___________________________________________


To create cache, put all of your caches and their values in one array of json objects structure 
and the array must be called "caches" as shown below

{
    "caches": [
        {
            "description": "",
            "diskSizeInMB": 0,
            "distributed": true,
            "expirySettings": {   
                "timeoutInSec": {  ### to make the expiration of a cache in amount of seconds
                    "value": "300"
                }
            },
            "inMemorySizeInKB": 0,
            "maxElementsInMemory": 0,
            "maxElementsOnDisk": 0,
            "name": "test5",
            "overflowToDisk": false,
            "persistent": false
        },
        {
            "description": "",
            "diskSizeInMB": 0,
            "distributed": true,
            "expirySettings": {
                "timeOfDay": {  ### to make the expiration of a cache in time of day
                    "value": "09:13:28"
                }
            },
            "inMemorySizeInKB": 0,
            "maxElementsInMemory": 0,
            "maxElementsOnDisk": 0,
            "name": "test2",
            "overflowToDisk": false,
            "persistent": false
        },
        {
            "description": "",
            "diskSizeInMB": 0,
            "distributed": true,
            "expirySettings": {
                "expiryDate": { ### to make the expiration of a cache in a specific date
                    "value": "02-24-2023"
                }
            },
            "inMemorySizeInKB": 0,
            "maxElementsInMemory": 0,
            "maxElementsOnDisk": 0,
            "name": "test3",
            "overflowToDisk": false,
            "persistent": false
        }
    ]
}