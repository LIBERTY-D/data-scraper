from cryptography.fernet import Fernet




def gen():
    key =  Fernet.generate_key()
    with open('key.txt','wb') as f:
        f.write(key)

# gen()

def read():
    with open('key.txt','rb') as f:
        key = f.read()
        return key


key = read()
# initialize the Fernet class




def fileEncryption(file,key):
    F= Fernet(key)
    data =b''
    with open(file,'rb') as f:
        data = f.read()
    with open(file,'wb') as f:
        f.write(F.encrypt(data))



# fileEncryption('test.txt',key)
def fileDecryption(file,key):
    F= Fernet(key)
    data =b''
    with open(file,'rb') as f:
        data = f.read()
    with open(file,'wb') as f:
        f.write(F.decrypt(data))


fileDecryption('test.txt',key)

