# -*- coding: utf-8 -*-
'''
WsseHeaders.utilities
~~~~~~~~~~~~~~
This module provides utility functions that are used within WsseHeaders
that are also useful for external consumption.
Note : but not currently exposed for external consumption
'''

import datetime
import base64
import hashlib
import sys
from Crypto import Random
from Crypto.Cipher import AES
import uuid
import pytz

class AESCipher(object):
    '''
    AES Cipher Class for Python
    '''

    def __init__(self, key, BS=AES.block_size):
        '''
        input : key (key to encrypt), BS (Block Size)
        '''
        self.bs = BS
        self.key = key

    def encrypt(self, raw, iv, padding=False):
        print(iv)
        if padding:
            raw = self._pad(raw)
        try:
            cipher = AES.new(self.key, AES.MODE_CFB, iv)
            return base64.b64encode(iv + cipher.encrypt(raw))
        except Exception as e:
            print(e)
            raise

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        try:
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
        except Exception as e:
            print(e)
            raise

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]



def generateDateString(zone=datetime.timezone.utc):
    '''
    generate a datetime string
    input : None
    return : datetime string of UTC 
    '''
    dateformat = str('%Y%m%d%H%M%S')
    curDate = datetime.datetime.now(tz=zone).replace(microsecond=0)
    return curDate.strftime(dateformat)


def generateISOTimeString(zone='UTC'):
    '''
    generate a datetime string in ISO 8601 format
    input : None (default_timezone = 'UTC')
    return : datetime string in ISO 8601 format
    '''
    tz = pytz.timezone(zone)
    curdate = tz.localize(datetime.datetime.now().replace(microsecond=0))
    return curdate.isoformat()
    

def generateMD5(string, algo='md5'):
    '''
    Function to return a md5 String
    input : string, algo=md5
    return : md5hash(string)
    '''
    m = hashlib.new(algo)
    string = string.encode('utf-8')
    m.update(string)
    return m.hexdigest()


def decode_Base64(encoded_string):
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
    Generate pseudo-random number and seconds since epoch (UTC)
    '''
    nonce = uuid.uuid4()
    oauth_timestamp, oauth_nonce = str(nonce.time), nonce.hex
    return oauth_nonce, oauth_timestamp


def generatePasswordDigest(nonce, timestamp, secret):
    concat_string = nonce + timestamp + secret
    try:
        sha1encoded = hashlib.sha1(concat_string.encode()).digest()
        encoded_sha1_string = base64.b64encode(sha1encoded)
        utf8encoded = encoded_sha1_string.decode('utf-8')
    except Exception as e:
        sys.stdout.write("Exception: %s\n"%(str(e)))
        sys.stdout.flush()
        raise
    return utf8encoded


