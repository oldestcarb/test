### 使用lxml的etree.iterparse()解析大型XML

有一个7G的大型xml需要解析，因为xml具有多层级，需要获取多个层级下的文本数据，使用sax事件驱动进行解析的话不方便获取数据，决定采用lxml的etree.iterparse()进行解析。
lxml 的 iterparse 方法是 ElementTree API 的扩展。iterparse 为所选的元素上下文返回一个 Python 迭代器。它接受两个有用的参数：要监视的事件元组和标记名。
参考：
> [Class iterparse](https://lxml.de/api/lxml.etree.iterparse-class.html)
> [Python解析巨型XML](https://www.jsome.net/blog/2010/08/18/handle-large-xml-with-python)  
> [使用由 Python 编写的 lxml 实现高性能 XML 解析](https://www.ibm.com/developerworks/cn/xml/x-hiperfparse/#resources)

完整代码如下:
```python
# -*- coding:utf-8 -*-

from lxml import etree
import time

def fast_iter(context, func, *args, **kwargs):
    """
    读取xml数据，并释放空间
    :params context: etree.iterparse生成的迭代器
    :params func:处理xml数据的func
    """
    # 事件、元素
    for event, elem in context:
        # 处理xml数据
        func(elem, *args, **kwargs)
        # 重置元素，清空元素内部数据
        elem.clear()
        # 选取当前节点的所有先辈（父、祖父等）以及当前节点本身
        for ancestor in elem.xpath('ancestor-or-self::*'):
            # 如果当前节点还有前一个兄弟，则删除父节点的第一个子节点。getprevious():返回当前节点的前一个兄弟或None。
            while ancestor.getprevious() is not None:
                # 删除父节点的第一个子节点，getparent()：返回当前节点的父元素或根元素或None。
                del ancestor.getparent()[0]
    # 释放内存
    del context

def process_element(elem):
    """
    处理element
    :params elem: Element
    """
    # 储存基因列表
    gene_list = []
    for i in elem.xpath('.//*[local-name()="gene"]/*[local-name()="name"]'):
        # 获取基因名字
        gene = i.text
        # 添加到列表
        gene_list.append(gene)
    
    print('gene', gene_list)
    
   

if __name__ == '__main__':
    print('start', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    start = time.time()

    # 文件路径
    infile = r'C:/Users/CRAB/Desktop/a.xml'
    # 通过迭代读取xml，带命名空间的要加上命名空间
    context = etree.iterparse(infile,events=('end',),encoding='UTF-8',tag='{http://uniprot.org/uniprot}entry')
    # 快速读取xml数据
    fast_iter(context,process_element)

    print('stop', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print('time', time.time()-start)

```