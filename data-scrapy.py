import requests,argparse,re,sys,os
from requests.exceptions import HTTPError


class RegX:

    def __init__(self,pattern,desc):
        self.pattern =pattern
        self.desc =  desc

  
phone =r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
email = r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)'
ip = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
link =r'[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)'

def FoundData(filename,data):
    # print(data)
    try:
        with open(filename,"w") as f:
                for info in data:
                    f.write(info)
                    f.write("\n")
            
    except Exception as err:
        print(err)
def scrapeFile(args,rgx):
    try:
        file = open(args.file,"rb")
        if(file.readable()):
            data = file.readline().decode()
            while data:
                response =  requests.get(data)
                for pat in rgx:
                    print("[*]LOOKING FOR "+pat.desc.upper() +" "+"FROM "+data)
                    info = re.findall(pat.pattern,response.text,re.I)
                    print("[*]FOUND "+pat.desc)
                    for d in range(len(info)):
                        print(f"[{d+1}]"+info[d]) 
                    FoundData("Found.txt",info)
                    print("FINISHED===================================!!!!!")   
                data = file.readline().decode()
    
        else:
            print("false")
        file.close()
      
    except Exception as err:
        print(err)
    

def scrapeUrl(args,rgx):
    try:
        response =  requests.get(args.url)
        response.raise_for_status()
        if(response.status_code==200):
             for pat in rgx:
                    print("[*]LOOKING FOR "+pat.desc.upper() +" "+"FROM "+args.url)
                    data = re.findall(pat.pattern,response.text,re.I)
                    print("[*]FOUND "+pat.desc)
                    for d in range(len(data)):
                        
                        print(f"[{d+1}]"+data[d]) 
                    print("FINISHED===================================!!!!!")   
                    FoundData("Found.txt",data)
        else:
            print("404")


    except HTTPError as err:
        print("[*]ERROR "+str(err))

     
def main(args):
    isFile =False
    rgx =[]
    emailP = RegX(email,"email")
    # phone pattern
    phoneP = RegX(phone,"phone")
    # IP address  pattern
    IPP = RegX(ip,"IP Address")
    # link pattern
    linkP = RegX(link,"link")
    if(args.url and args.url.startswith("http") and not isFile):
        if(args.scraper=="e"):
            rgx=[emailP]
        
        elif(args.scraper=="i"):
            rgx=[IPP]
        elif(args.scraper=="p"):
            rgx=[phoneP]
        elif(args.scraper=="l"):
            rgx = [linkP]
        elif(args.scraper=="a"):
            rgx=[emailP,phoneP,IPP,linkP]
        scrapeUrl(args,rgx)
    elif(args.file):
        isFile=True
        if(args.scraper=="e"):
            rgx=[emailP]
        
        elif(args.scraper=="i"):
            rgx=[IPP]
        elif(args.scraper=="p"):
            rgx=[phoneP]
        elif(args.scraper=="a"):
            rgx=[emailP,phoneP,IPP,linkP]
        scrapeFile(args,rgx)

        



     
        
       
    



if (__name__ =="__main__"):
    parser = argparse.ArgumentParser()
    parser.add_argument("-url",action="store", type=str,help="enter url to scrape")
    parser.add_argument("-file",action="store",type=str,help="enter file location" ,nargs="?")
    parser.add_argument("-scraper",nargs="?",type=str,action="store",help="e=email,p=phone number,i=Ip Address ,l=link, a=all",default="a")
    args =  parser.parse_args()
    if(len(sys.argv[1:])==0):
        parser.print_help()
        parser.exit()

    main(args)
    
    