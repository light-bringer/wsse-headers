# -*- coding: utf-8 -*-

import base64
from AES import AESCipher
from . import utilities as utils



class WsseToken():
    '''
    WSSE Token 
    '''
    
    def getDateTime(self):
        '''
        get Date value
        '''
        return str(self.__DateString)
    

    def getOrg(self):
        '''
        get Organisation value
        '''
        return str(self.__Organization)
    

    def getUser(self):
        '''
        get User value
        '''
        return str(self.__UserName)
    

    def __str__(self):
        '''
        str function
        '''
        return  str(self.__class__) + '\n'+ '\n'.join(('{} = {}, {}'.format(item, self.__dict__[item], type(self.__dict__[item])) for item in self.__dict__))


    def __init__(self, username, orgName, token):
        '''
        init function
        '''
        if username is None or username is "":
            raise ValueError
        elif orgName is None or orgName  is "":
            raise ValueError
        elif token is None or len(token) < 16:
            raise ValueError      
        self.__UserName = username
        self.__Organization = orgName
        self.__TOKEN = token
        self.__DateString = utils.generateISOTimeString()
        secret_key = utils.generateMD5(self.__UserName)
        iv = utils.decode_Base64(self.__TOKEN)
        self.base64iv = iv[:16]
        AES_obj = AESCipher(secret_key)
        self.__secret = AES_obj.encrypt(raw=self.__TOKEN, iv=self.base64iv, padding=False)
        self.__b64_nonce, self.__nonce = utils.generate_nonce()


    def generateHeaderString(self):
        '''
        generate WSSE Header String
        '''
        try:
            self.__PasswordDigest = utils.generatePasswordDigest(
                self.__nonce, self.__b64_nonce, self.__DateString, self.__secret.decode('ASCII')
            )
            header = 'UsernameToken Username="%s", PasswordDigest="%s", Nonce="%s", Created="%s", Organization="%s"'%(
                self.__UserName,
                self.__PasswordDigest, 
                self.__b64_nonce.decode() , self.__DateString, 
                self.__Organization)
            return header
        except Exception as e:
            print(e)
            raise


    def generateHeader(self):
        '''
        returns a dictionary with the WsseString
        '''
        return {
            'Authorization': 'WSSE profile="UsernameToken"',
            'X-WSSE': self.generateHeaderString(),
            'Accept':'Application/json'
        }
