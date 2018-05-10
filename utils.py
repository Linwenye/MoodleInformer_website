import requests
from Crypto.Cipher import AES
import config


def verify(email, password):
    url = 'http://218.94.159.99/login/index.php'
    formdata = {
        'username': email,
        'password': password,
        'rememberusername': '1'
    }

    r = requests.post(url=url, data=formdata)
    if '登录无效' in r.text:
        return False
    else:
        return True


def encrypt(msg):
    cipher = AES.new(encrypt_key, AES.MODE_CFB, iv)
    encrypted_msg = cipher.encrypt(msg)
    return encrypted_msg


# # when incorrect encryption key is used, `decrypt` will return empty string
def decrypt(msg):
    cipher = AES.new(encrypt_key, AES.MODE_CFB, iv)
    return cipher.decrypt(msg)


BS = 16
encrypt_key = config.SECRET_KEY
iv = config.SECRET_IV
