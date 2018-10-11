# -*- coding: utf-8 -*-

from . import utilities as utils


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

    
    def __init__(self, username, orgName, token):
        self.__UserName = username
        self.__Organization = orgName
        self.__AuthToken = token
        self.__DateString = utils.generateISOTimeString()
        key = utils.generateMD5(self.__UserName)
        iv = utils.decode_Base64(self.__AuthToken)
        base64iv = utils.base64.b64encode(iv.encode())
        AESObj = utils.AESCipher(key)
        self.__secret = AESObj.encrypt(token, base64iv)
        self.__nonce = utils.generate_nonce()[0]

    def generateHeaders(self):
        passworddigest = utils.generatePasswordDigest(
            self.__nonce, self.__DateString, self.__secret.decode('ASCII')
        )
        header = "UsernameToken Username=%s, PasswordDigest=%s, \
        Nonce=%s, Created=%s, Organization=%s"%(
            self.__UserName,
            passworddigest, 
            self.__nonce , self.__DateString, 
            self.__Organization)
        return header

