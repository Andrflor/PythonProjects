#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, crypt,hashlib
from threading import Thread

def encrypt(passphrase):
    crypted = crypt.crypt(passphrase,"HX")
    return crypted

def sha512_encrypt(passphrase):
    return hashlib.sha512(passphrase.encode(encoding='utf_8')).hexdigest()

if len(sys.argv)>=2:
    myCryptedPass = sys.argv[1]
else:
    myCryptedPass = sha512_encrypt("tr0l")

if len(sys.argv)>=3:
    filename = sys.argv[2]
else:
    filename = "dictionary.txt"


def dicoToList():
    fileStream = open(filename,"r")
    dicoToString = fileStream.read()
    return dicoToString.split(' ')

def decrypt(cryptedPhrase):
    dictio = dicoToList()
    for element in dictio:
        """
        t = Thread(target=sha512_encrypt, args=element)
        t.start()
        """
        if sha512_encrypt(element)==cryptedPhrase:
            return element

    return "Password not found"

if __name__=="__main__":
    password = decrypt(myCryptedPass)
    print(password)
