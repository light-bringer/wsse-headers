import utilities as utils


class WsseToken():
    # _UserName = None
    # _Organization = None
    # _AuthToken = None
    # _DateString = None

    
    def getdate(self):
        return str(self.__DateString)
    

    def getOrg(self):
        return str(self.__Organization)
    

    def getUser(self):
        return str(self.__UserName)

    
    def __init__(self, username, orgName, token):
        self.__UserName = username
        self.__Organization = orgName
        self.__AuthToken = token
        self.__DateString = utils.gendate()
        print("fuck you")


a = WsseToken("", "", "")
a.__init__("", "", "")
