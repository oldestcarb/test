### lxml的etree.iterparse()解析大型XML遇到命名空间的问题


 需要解析一个7G的大型xml，因为xml具有多层级，需要获取多个层级下的文本数据，决定采用lxml的etree.iterparse()进行解析。
参考：
> [Python解析巨型XML](https://www.jsome.net/blog/2010/08/18/handle-large-xml-with-python)  
> [使用由 Python 编写的 lxml 实现高性能 XML 解析](https://www.ibm.com/developerworks/cn/xml/x-hiperfparse/#resources)


需要解析的xml文件预览如下：
```xml
<uniprot xmlns="http://uniprot.org/uniprot" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://uniprot.org/uniprot http://www.uniprot.org/support/docs/uniprot.xsd">
<entry dataset="Swiss-Prot" created="1994-06-01" modified="2019-02-13" version="170">
<accession>Q00604</accession>
<accession>B2R8K6</accession>
<accession>Q5JYH5</accession>
<name>NDP_HUMAN</name>
<protein>
<recommendedName>
<fullName>Norrin</fullName>
</recommendedName>
<alternativeName>
<fullName>Norrie disease protein</fullName>
</alternativeName>
<alternativeName>
<fullName>X-linked exudative vitreoretinopathy 2 protein</fullName>
</alternativeName>
</protein>
</entry>
</uniprot>
```

参照上述参考文章的代码，无法输出有效内容，检查好几遍代码都不行。
```python 
from lxml import etree

if __name__ == '__main__':

    infile = r'C:/Users/CRAB/Desktop/uniprot_sprot.xml/uniprot_sprot.xml'
    context = etree.iterparse(infile, events=('end',), encoding='UTF-8', tag='entry')
    for event, elem in context:
        print(elem.xpath('.//protein'))
```

后来经过google,发现是命名空间的问题。
即xml文件开头`uniprot`标签的几个属性。
```
xmlns="http://uniprot.org/uniprot" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://uniprot.org/uniprot http://www.uniprot.org/support/docs/uniprot.xsd"
```
关于xml命名空间，参考：
> [关于XML文档的xmlns、xmlns:xsi和xsi:schemaLocation](https://www.cnblogs.com/zhao1949/p/5652167.html)

在lxml中，如果有命名空间，获取标签的表达式有所变化。
参考官方文档：
> [namespaces](https://lxml.de/tutorial.html#namespaces)
> [namespaces-and-prefixes](https://lxml.de/xpathxslt.html#namespaces-and-prefixes)

即：
```
context = etree.iterparse(infile,events=('end',),encoding='UTF-8',tag='entry')
```
中`tag`的写法要加上命名空间，如下：
```python
# xml开头中的： xmlns="http://uniprot.org/uniprot"
# {http://uniprot.org/uniprot} 为命名空间
context = etree.iterparse(infile, events=('end',), encoding='UTF-8', tag='{http://uniprot.org/uniprot}entry')
```
这样就可以获取到结果。同时，表达式也要改变：
```python
# 一般写法
elem.xpath('.//protein')
# 带命名空间的写法
elem.xpath('.//*[local-name()="protein"]')

```


具体方法请参考官方文档,引用如下：

Just like the xpath() method, the XPath class supports XPath variables:
```
>>> count_elements = etree.XPath("count(//*[local-name() = $name])")

>>> print(count_elements(root, name = "a"))
1.0
>>> print(count_elements(root, name = "b"))
2.0
```
This supports very efficient evaluation of modified versions of an XPath expression, as compilation is still only required once.

Prefix-to-namespace mappings can be passed as second parameter:
```
>>> root = etree.XML("<root xmlns='NS'><a><b/></a><b/></root>")

>>> find = etree.XPath("//n:b", namespaces={'n':'NS'})
>>> print(find(root)[0].tag)
{NS}b
```
使用lxml的etree.iterparse()解析大型XML的完整代码链接
- [aa]()