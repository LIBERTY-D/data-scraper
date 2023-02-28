import socket,argparse,sys



class PORT:
    def __init__(self,ip,sport,fport):
        self.ip = ip
        self.sport  = sport
        self.fport = fport

   
    
    def scanPorts(self):
         for p in range (self.sport,self.fport):
                try:

                    s = socket.socket()
                    s.connect((self.ip,p))
                    print("[+]OPEN {}:{}".format(self.ip,p))
                    s.close()
                except:
                    print("[-]CLOSED {}:{}".format(self.ip,p))
            

                
                
        
    def main(self,args):
        if args.ip and args.sp and args.fp :
            self.scanPorts()
        



parser  = argparse.ArgumentParser()
parser.add_argument("-ip",help="enter target ip",action="store",type=str)
parser.add_argument("-sp",help="start port",action="store",nargs="?",default=1,type=int)
parser.add_argument("-fp",help="final port",action="store",type=int)
args =  parser.parse_args()

if(len(sys.argv[2:])==0):
    parser.print_help()
    parser.exit()


if __name__=="__main__":
      if args.ip and args.sp and args.fp :
         port  =  PORT(args.ip,args.sp,args.fp+1)
         port.main(args)
      else:
        parser.print_help()
        parser.exit()


