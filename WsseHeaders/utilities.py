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
import uuid
import pytz
import string
import random


__NONCE_LENGTH__ = 16
__NONCE_METHOD_UUID__ = 0
__NONCE_METHOD_RANDOM__ = 1




def generateDateString(zone='UTC'):
    '''
    generate a datetime string
    input : None
    return : datetime string of UTC 
    '''
    dateformat = str('%Y%m%d%H%M%S')
    curDate = datetime.datetime.utcnow(tz=zone).replace(microsecond=0)
    return curDate.strftime(dateformat)




def generateISOTimeString(zone='utc'):
    '''
    generate a datetime string in ISO 8601 format
    input : None (default_timezone = 'UTC')
    return : datetime string in ISO 8601 format
    '''
    tz = pytz.timezone(zone)
    curdate = tz.localize(datetime.datetime.utcnow().replace(microsecond=0))
    return curdate.isoformat()




def generateMD5(string, algo='md5'):
    '''
    Function to return a md5 String
    input : string, algo=md5
    return : md5hash(string)
    '''
    m = hashlib.new(algo)
    string = string.encode('ascii')
    m.update(string)
    return m.hexdigest()




def decode_Base64(encoded_string):
    '''
    take a base64 string as <str> and decode it to original string as <str>
    input : encoded_string
    output : decoded_string
    '''
    try:
        decodedstring = base64.b64decode(encoded_string.encode()).decode('ascii')
    except Exception as e:
        sys.stdout.write("Exception: %s\n"%(str(e)))
        sys.stdout.flush()
        raise

    return decodedstring




def generate_nonce(length=__NONCE_LENGTH__, default_method=__NONCE_METHOD_RANDOM__):
    '''
    Generate a random number
    '''
    if default_method == __NONCE_METHOD_RANDOM__:
        random_str = get_random_ascii_string(length=length*2)
        nonce = hashlib.md5(random_str.encode()).digest()[0:length]
    elif default_method == __NONCE_METHOD_UUID__:
        random_str = str(uuid.uuid4()).encode('ascii')
        nonce = hashlib.md5(random_str).digest()[0:length]
    else:
       raise Exception('Unknown random method to create nonce')
    
    nonce_base64 = base64.b64encode(nonce)
    return nonce_base64,nonce




def generatePasswordDigest(nonce, b64_nonce, timestamp, secret):
    nonce = base64.b64decode(b64_nonce)
    concat_string_byte = nonce + timestamp.encode('ascii') + secret.encode()
    try:
        hashd = hashlib.sha1()
        hashd.update(concat_string_byte)
        hash_digest = hashd.digest()
        pwd_digest = base64.b64encode(hash_digest)
        ascii_pwd_digest = pwd_digest.decode('ascii')
    except Exception as e:
        sys.stdout.write("Exception: %s\n"%(str(e)))
        sys.stdout.flush()
        raise
    return ascii_pwd_digest




def get_random_ascii_string(length=__NONCE_LENGTH__, allowed_chars=None):
    '''
    source: https://github.com/PrincetonUniversity/pywsse/blob/master/wsse/utils.py
    Generate a random string of the given length.
    :param length: length of the string (defaults to settings.NONCE_LENGTH)
    :rtype length: int
    :param allowed_chars: characters to allow in string
    :rtype allowed_chars: str
    :return: generated string
    :rtype: str
    '''
    if allowed_chars is None:
        try:
            allowed_chars = string.digits
        except AttributeError:
            allowed_chars = string.digits
    else:
        try:
            allowed_chars = string.letters
        except AttributeError:
            allowed_chars = string.ascii_letters
    
    if length is None:
        length = __NONCE_LENGTH__
    
    randomstr = ''.join(random.choice(allowed_chars) for _ in range(length))
    
    return randomstr
