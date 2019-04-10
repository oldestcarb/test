import re

url = 'https://www.genecopoeia.com/order/'
real_url = re.sub(r'\/$', '', url)
print(real_url)