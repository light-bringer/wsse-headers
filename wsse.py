import base64
import hashlib
import datetime
import uuid
import string
import random


from Crypto.Cipher import AES

NONCE_LENGTH = 16
NONCE_METHOD_UUID = 0
NONCE_METHOD_RANDOM = 1

def get_random_string(length=None, allowed_chars=None):
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
           allowed_chars = string.letters
       except AttributeError:
           allowed_chars = string.ascii_letters

   if length is None:
       length = NONCE_LENGTH

   s = ''.join(random.choice(allowed_chars) for _ in range(length))
   return s


def get_nonce(length=NONCE_LENGTH, default_method=NONCE_METHOD_RANDOM):
   '''
   Returns a random string, plan and encoded
   :return:
   '''
   if default_method == NONCE_METHOD_UUID:
       random_str = str(uuid.uuid4()).encode('ascii')
       nonce = hashlib.md5(random_str).digest()[0:length]
   elif default_method == NONCE_METHOD_RANDOM:
       random_str = get_random_string(length=length*2)
       nonce = hashlib.md5(random_str).digest()[0:length]
   else:
       raise Exception('Unknown random method to create nonce')
   nonce_base64 = base64.b64encode(nonce)
   return (nonce, nonce_base64)

def generate_secret_key(user_name):
   return hashlib.md5(user_name.encode('ascii')).hexdigest()


def generate_secret_vi(token):
   iv = base64.b64decode(token)[0:16]
   return iv


def generate_secret(user_name, token):
   secret_key = generate_secret_key(user_name)
   secret_vi = generate_secret_vi(token)
   mode = AES.MODE_CFB
   cipher = AES.new(secret_key, mode, secret_vi, segment_size=8*AES.block_size)
   encrypted = cipher.encrypt(token)
   secret = base64.b64encode(secret_vi + base64.b64encode(encrypted).decode())
   return secret


def generate_pwd_digest(user_name, nonce_base64, token, current_time_string):
   nonce = base64.b64decode(nonce_base64)
   secret = generate_secret(user_name, token)
   hash_digest = hashlib.sha1()
   hash_digest.update(nonce + current_time_string.encode('ascii') + secret)
   pwd_digest = base64.b64encode(hash_digest.digest())
   return pwd_digest

def generate_timestamp_string():
   '''
   Return in a format, with timezone, in utc, and no miliseconds
   2018-09-28T16:12:56+00:00
   :return: now in format like above
   '''
   return datetime.datetime.utcnow().replace(microsecond=0).replace(tzinfo=utc).isoformat()


def generate_header(user_name, token, organisation):
   nonce, nonce_base64 = get_nonce()
   current_time_string = generate_timestamp_string()
   password_digest = generate_pwd_digest(user_name, nonce_base64, token, current_time_string)
   x_wsse = ', '.join(['UsernameToken Username="{user}"',
                       'PasswordDigest="{pwd_digest}"',
                       'Nonce="{nonce}"',
                       'Created="{created}"',
                       'Organization="{organization}"'])
   x_wsse = x_wsse.format(
                       user=user_name,
                       pwd_digest=password_digest,
                       nonce=nonce_base64,
                       created=current_time_string,
                       organization=organisation
                   )

   return {
           'Authorization': 'WSSE profile="UsernameToken"',
           'X-WSSE': x_wsse,
           'Accept':'application/json'
          }