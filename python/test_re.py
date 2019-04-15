import re
real_url = '/html/question/201904/408542.shtml'
a = re.search(r'question\/\d+\/\d+\.shtml', real_url)
print(a)