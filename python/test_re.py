import re
count = 0
url1 = 'https://www.genecopoeia.com/orderlin'
url2 = 'https://www.genecopoeia.com/prosdusdct/search3/result.php?key=HmiRQP0037&prt=15&field=11'
url3 = 'https://www.genecopoeia.com/orderesult.php?key=HmiRQ'
url4 = 'https://www.genecopoeia.com/product/search/result.php?key=HmiRQP0037&prt=15&field=11'
url5 = 'https://www.genecopoeia.com/product/search/detail.php?prt=19&cid=&key=HQP009693'
url6 = 'https://www.genecopoeia.com/order/'
IGNORE_URL = [
    'login',
    '.com/order',
    '.com/product/search',
    '.com/product/search2',
    '.com/product/search3',
    '.pdf',
    '.jpg',
    '.png',
    '.gif',
    '.jpeg',
    '.xls',
    '.lxls'
]
def add( url): 
    count = 0
    print(count)
    for i in IGNORE_URL:
        pattern = re.compile(i, re.I)
        # print(pattern.search(url))
        if pattern.search(url):
            count += 1
    print()
    if count:
        return 
    print(url)

add(url6)
add(url2)
add(url3)
add(url4)