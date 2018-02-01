import sys, crypt

def encrypt(passphrase):
    crypted = crypt.crypt(passphrase,"HX")
    return crypted
    
if __name__=="__main__":
    if len(sys.argv)==2:
        res = encrypt(sys.argv[1])
        print("Encrypted_Word = %s" % res)
