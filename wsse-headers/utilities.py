# -*- coding: utf-8 -*-

import datetime
import base64
import hashlib
import sys
from Crypto import Random
from Crypto.Cipher import AES
import uuid

class AESCipher(object):

    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]



def gendate(zone=datetime.timezone.utc):
    '''
    generate a datetime string
    input : None
    return : datetime string of UTC 
    '''
    dateformat = str('%Y%m%d%H%M%S')
    curDate = datetime.datetime.now(tz=zone).replace(microsecond=0)
    return curDate.strftime(dateformat)


def getmd5(string, algo='md5'):
    '''
    Function to return a md5 String
    input : string, algo=md5
    return : md5hash(string)
    '''
    m = hashlib.new(algo)
    string = string.encode('utf-8')
    m.update(string)
    return m.hexdigest()


def decode_base64(encoded_string):
    '''
    take a base64 string as <str> and decode it to original string as <str>
    input : encoded_string
    output : decoded_string
    '''
    b64str = encoded_string.encode()
    try:
        string = base64.b64decode(b64str).decode('utf-8')
    except Exception as e:
        sys.stdout.write("Exception: %s\n"%(str(e)))
        sys.stdout.flush()
        raise

    return string


def generate_nonce():
    '''
    Generate pseudo-random number and seconds since epoch (UTC).
    '''
    nonce = uuid.uuid4()
    oauth_timestamp, oauth_nonce = str(nonce.time), nonce.hex
    return oauth_nonce, oauth_timestamp





