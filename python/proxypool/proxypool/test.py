import re
proxy =  '1.1.1.1:111'
juege_proxy = re.search('(.*):', proxy).group(1)

print(juege_proxy)