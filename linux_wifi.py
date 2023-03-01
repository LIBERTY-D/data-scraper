#!/usr/bin/python3
import configparser
import os

config = configparser.ConfigParser()

profiles =[]
path = "/etc/NetworkManager/system-connections/"
files= os.listdir(path)

    
if(len(files)>0):
    for file in files:
        fullPath = os.path.join(path,file)
        config.read(fullPath)
        sections = config.sections()
        if(len(sections)>0):
            for f in range(len(sections)):
                temp ={}
                if("wifi-security"== sections[f]):
                    data =  config[sections[f]]
                    for key in data:
                        value =  config[sections[f]][key]
                        temp[key] = value
                        temp["ssid"] = config["wifi"]["ssid"]
                    profiles.append(temp)
                
                    


# Print out the password

print("auth-alg"+" "*20,"ssid"+" "*20,"key-mgmt"+" "*20,"psk"+" "*20)
for dic in range(len(profiles)):
    print("{:28} {:28} {:28} {:28}".format(profiles[dic]['auth-alg'],profiles[dic]['ssid'],profiles[dic]['key-mgmt'],profiles[dic]['psk']))
            
                        
                        
                        
                    
  
 