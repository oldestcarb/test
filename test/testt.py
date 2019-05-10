from urllib.parse import urlencode, parse_qs, quote, unquote

data = {
    'q':'知道',
    'name':'aa'
}
url = 'https://www.baidu.com?'

# urlencode() 方法将其序列化为 URL 标准 GET 请求参数
encode_data = urlencode(data)

print(url + encode_data)
# https://www.baidu.com?q=%E7%9F%A5%E9%81%93&name=aa

print(parse_qs(encode_data))
# {'q': ['知道'], 'name': ['aa']}

# 将内容转化为 URL 编码的格式
print(quote('知道'))
# %E7%9F%A5%E9%81%93
print(unquote(r'%E7%9F%A5%E9%81%93'))