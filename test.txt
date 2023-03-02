
from scapy.all import *
import sys

try:

    if(len(sys.argv)!=2):
        print("Provide the required arguments")
        sys.exit(1)
    ether =Ether(dst='ff:ff:ff:ff:ff:ff',)
    arp = ARP(pdst=sys.argv[1])

    ans,uns =  srp(ether/arp,timeout=2)

    clients=[]
    for snd,rcv in ans:
        print(rcv.summary())
        # print(snd.summary(),"\n",rcv.summary())
        clients.append({"ip":rcv.psrc,"mac":rcv.hwsrc,"macsrc":rcv.hwdst,"ipsrc":rcv.pdst})


    print(clients)
    # space between
    print("IP" + " "*20+"MAC"+ " "*20+"ipsrc" + " "*20+"macsrc")
    for client in clients:
        print("{:16}      {}   {}   {}".format(client['ip'], client['mac'], client['ipsrc'],client['macsrc']))
except KeyboardInterrupt as err:
    print("[*]Exited")
    sys.exit(1)