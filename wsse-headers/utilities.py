# -*- coding: utf-8 -*-

import datetime
import base64
import hashlib
import sys

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
    b64str = encoded_string.encode()
    try:
        string = base64.b64decode(b64str).decode('utf-8')
    except Exception as e:
        sys.stdout.write("Exception: %s\n"%(str(e)))
        sys.stdout.flush()
        raise

    return string




