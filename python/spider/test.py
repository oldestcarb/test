import requests

url = "https://www.baidu.com"

headers = {"user-agent":"","connection":"keep-alive"}

kw = {"wd":"baidu"}

proxies = {
    "http":"http://1.1.1.1:111"
    "https":"https://2.2.2.2:222"
}

formdata = {
    "type":"auto",
    "i":"i love python",
    "ue":"utf-8"
    "email":"",
    "passwd":""
}

auth = ("test","123456")

sess = requests.session()

response = requests.get(url, params = kw, headers = headers, proxies = proxies, verify = True)

responses = sess.get(url, data = formdata, headers = headers, auth = auth)

cookkk = sess.get()

