import subprocess,random,re,string



def randMac():
    hex = "".join(set(string.hexdigits.upper()))
    choices ="02468ACE"
    mac ="" 
    for i in  range(6):
        for l in range(2):
            if(l==0):
                mac+=random.choice(choices)
            else:
                mac+=random.choice(hex)
        mac+=":"
    return mac.strip(":")





def originalMac(iface):
    # use the ifconfig command to get the interface details, including the MAC address
    output = subprocess.check_output(f"ifconfig {iface}", shell=True).decode()
    data = re.search("ether (.+)",output).group().split(" ")[1].strip()
    return data



def changeMac(iface,newMac):
    # disable the network interface
    subprocess.check_output(f"ifconfig {iface} down", shell=True)
    # change the MAC
    subprocess.check_output(f"ifconfig {iface} hw ether {newMac}", shell=True)
    # enable the network interface again
    subprocess.check_output(f"ifconfig {iface} up", shell=True)

original = originalMac("wlp2s0")
rand =  randMac()
changeMac("wlp2s0",rand)
print("[original mac] "+original)
print("[random] "+rand)
