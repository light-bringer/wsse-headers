from Crypto.Cipher import AES
import base64



class AESCipher(object):
    '''
    AES Cipher Class for Python
    '''
    def __str__(self):
        return  str(self.__class__) + '\n'+ '\n'.join(('{} = {}, {}'.format(item, self.__dict__[item], type(self.__dict__[item])) for item in self.__dict__))


    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    
    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    
    def __init__(self, key, BS=AES.block_size, mode=AES.MODE_CFB):
        '''
        input : key (key to encrypt), BS (Block Size)
        '''
        self.bs = BS
        self.key = key
        self.mode = mode
        self.__pad = lambda s: s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)


    def encrypt(self, raw, iv, padding=False):
        '''
        Encrypt : encrypt a raw string from an iv
        '''
        if padding:
            raw = self.__pad(raw)
        try:
            cipher = AES.new(key=self.key.encode(), mode=self.mode, IV=iv.encode(), segment_size=8*self.bs)
            encrypted = cipher.encrypt(raw.encode())
            secret = base64.b64encode((iv.encode() + base64.b64encode(encrypted)))
            return secret
        except Exception as e:
            print(e)
            raise


    def decrypt(self, enc):
        '''
        Decrypt : decrypt a raw string from an iv
        '''
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        try:
            cipher = AES.new(self.key, self.mode, iv, segment_size=8*AES.block_size)
            return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('ascii')
        except Exception as e:
            print(e)
            raise
    
