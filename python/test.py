from requests import Request
from requests import Session

class WeixinRequest(Request):
    def __init__(self, url, method='GET', headers=None, timeout=5):
        super(WeixinRequest, self).__init__(method, url, headers)
        self.timeout = timeout
        
if __name__ == '__main__':
    session = Session()
    headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    url = 'https://www.baidu.com'
    weixin = WeixinRequest(url=url)
    print(session.headers)
    session.headers.update(headers)
    print(session.headers)
    # response = session.send(weixin.prepare())
    response = session.send(session.prepare_request(weixin))
    print(response.request.headers)