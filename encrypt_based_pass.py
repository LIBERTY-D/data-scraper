import cryptography
from cryptography.fernet import Fernet,InvalidToken
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import getpass
import base64
import secrets
import argparse
import sys
from pathlib import Path



# generate salt
def salt():
    secret = secrets.token_bytes()
    return secret

# write salt to file
def writeSaltToFile(filename):
    secret=salt()
    with open(filename,'wb') as file:
        file.write(secret)

# read salt
def readSaltFromFile(filename):
    with open(filename,'rb') as file:
        data = file.read()
        return data

# derive key from the password
def deriveKeyFromPass(salt,password):
    kdf = Scrypt(salt=salt,length=32,n=2**14,r=8,p=1)
    derive =  kdf.derive(password.encode())
    return base64.urlsafe_b64encode(derive)

# write key to file
def writeKeyToFile(filename,key):
    with open(filename,'wb') as file:
        file.write(key)




# main function
def main(args):
        salt =b''
        if  (not Path('salt.salt').is_file()):
            print('no such file')
            salt = writeSaltToFile('salt.salt')
        else:
            salt = readSaltFromFile('salt.salt')
            if ((args.e=='yes' and args.d=='yes')):
                print('[+] You cant do encrypt and decrypt at the same time')
                sys.exit(1)
            elif args.e=='yes':
                print('ENCRYPTING PROCESS...')
                password = getpass.getpass()
                if password =='':
                    print('Password cannot be empty')
                    exit()
                else:
                    key  =  deriveKeyFromPass(salt,password)
                    writeKeyToFile('key.txt',key)
                    encryptData(args.file,key)

            elif args.d=='yes':
                    print('DECRYPTING PROCESS,..')
                    password = getpass.getpass('Enter same Password You used to encrypt: ')
                    if password =='':
                        print('Password cannot be empty')
                        sys.exit(1)
                    else:
                        
                        key  =  deriveKeyFromPass(salt,password)
                        writeKeyToFile('key.txt',key)
                        decryptData(args.file,key)

    
def readData(filename):
    with open(filename,'rb') as file:
        info = file.read()
        return info

def encryptData(filename,key):
    F = Fernet(key=key)
    data = readData(filename)
    with open(filename,'wb') as file:
        file.write(F.encrypt(data))

def decryptData(filename,key):
    F = Fernet(key=key)
    data = readData(filename)
    try:
        decrypted =F.decrypt(data)
        with open(filename,'wb') as file:
            file.write(decrypted)

    except InvalidToken as err:
        print('[Your Password Is Incorrect] ',err)
    
    





parser =  argparse.ArgumentParser()
parser.add_argument('-s',help='salt to encrypt your pass',nargs='?',type=int,default=1)
parser.add_argument('-file',help='file to encrypting and decrypting',action='store' ,type=str)
parser.add_argument('-e',help='for encrypting', action='store' ,nargs='?',type=str,default='no')
parser.add_argument('-d',help='for decrypting',action='store',nargs='?',type=str,default='no')
args = parser.parse_args()

if(len(sys.argv[2:])==0):
    parser.print_help()
    parser.exit()
if __name__=='__main__':
    main(args)


