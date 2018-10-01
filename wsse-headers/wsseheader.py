import datetime


class WsseToken():
    _curDate = None
    _UserName = None
    _Organization = None
    _AuthToken = None
    _DateString = None

    def gendate(self):
        self.curDate = datetime.datetime.now().replace(microsecond=0)
        self.DateString = self.curDate.strftime('YYYYMMDDHHMM')
    def __init__(self, username, orgName, token):
        self._UserName = username
        self._Organization = orgName
        self._AuthToken = token
        self._curDate = datetime.datetime.now().replace(microsecond=0)


