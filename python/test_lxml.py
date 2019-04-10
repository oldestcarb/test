from lxml import etree

a = """<div>
    <ul class="1">test
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
# c = b.xpath('string(//ul[2])')
# c = b.xpath('string(//ul[@class="2"])')
c = b.xpath('//ul')[1].xpath('string(.)')
print(c)