# -*- coding: utf-8 -*-

from . import utilities as utils
import base64


class WsseToken():
    # _UserName = None
    # _Organization = None
    # _AuthToken = None
    # _DateString = None

    
    def getDateTime(self):
        return str(self.__DateString)
    

    def getOrg(self):
        return str(self.__Organization)
    

    def getUser(self):
        return str(self.__UserName)
    

    def __str__(self):
        return  str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))


    def __init__(self, username, orgName, token):
        if username is None or username is "":
            raise ValueError
        elif orgName is None or orgName  is "":
            raise ValueError
        elif token is None or len(token) < 16:
            raise ValueError
            
        self.__UserName = username
        self.__Organization = orgName
        self.__TOKEN = token
        self.__AuthToken = token[:16]
        self.__DateString = utils.generateISOTimeString()
        secret_key = utils.generateMD5(self.__UserName)
        print(self.__AuthToken)
        iv = utils.decode_Base64(self.__AuthToken)
        print(iv, secret_key)
        base64iv = base64.b64encode(iv.encode())
        AESObj = utils.AESCipher(secret_key)
        self.__secret = AESObj.encrypt(self.__AuthToken, base64iv)
        self.__b64_nonce, self.__nonce = utils.generate_nonce()
        print(self.__b64_nonce.decode(), self.__nonce)

    def generateHeaders(self):
        try:
            passworddigest = utils.generatePasswordDigest(
                self.__nonce, self.__b64_nonce, self.__DateString, self.__secret.decode('ASCII')
            )
            header = 'UsernameToken Username="%s", PasswordDigest="%s", Nonce="%s", Created="%s", Organization="%s"'%(
                self.__UserName,
                passworddigest, 
                self.__b64_nonce.decode() , self.__DateString, 
                self.__Organization)
            return header
        except Exception as e:
            print(e)
            raise



