import requests


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
