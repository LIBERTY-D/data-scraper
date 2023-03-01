#!/usr/bin/python3
import subprocess,argparse,sys



def currentIp(iface):
    try:
        # display current Ip setting
        res=subprocess.check_output(f"ifconfig {iface}",shell=True).decode()
        print(res)
    except Exception as err:
        print(err)

def changeLinuxIp(ip,iface,netmask):
    subprocess.check_output(f"ifconfig {iface} inet {ip} netmask {netmask} ",shell=True)
    print("Your new IP")
    currentIp("wlp2s0")
    

def main(args):
    print("Your Current IP")
    currentIp("wlp2s0")
    if(args.i and args.iface,args.net):
        changeLinuxIp(args.i,args.iface,args.net)

    


parser =  argparse.ArgumentParser()
parser.add_argument("-i",action="store",help="Enter new Ip Address")
parser.add_argument("-iface",action="store",help="Enter Your Network Interface")
parser.add_argument("-net",action="store",help="your netmask")
args = parser.parse_args()

if(len(sys.argv[2:])==0):
    parser.print_help()
    parser.exit()


if __name__=="__main__":
    main(args)