from lxml import etree

a = """<div>
    <ul class="1">
        <li>1</li>
        <li>12<a>bcd</a></li>
        <li>123</li>
        <li>1234</li>
    </ul>
    <ul class="2">
        <li>2</li>
        <li>22<a>bcd</a></li>
        <li>223</li>
        <li>2234</li>
    </ul>
</div>
    """
b = etree.HTML(a)
c = b.xpath('//ul')[1].xpath('string(.)')
print(c)
# d = c.replace('\n','')
# d = d.replace(' ','')
# for i in c:
#     print(i)
# print(str(c),type(str(c)))

# string text 区别
# string两种方式 数量 结果类型