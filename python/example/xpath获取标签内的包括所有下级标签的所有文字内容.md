### xpath获取标签内的包括所有下级标签的所有文字内容
现有html源码如下:
```html
<div>
    <ul class="1">
        <li>1</li>
        <li>12<a>bcd</a></li>
        <li>123</li>
        <li>1234</li>
    </ul>
    <ul class="2">
        <li>2</li>
        <li>22<a>efg</a></li>
        <li>223</li>
        <li>2234</li>
    </ul>
</div>
```
想要获取`ul class="1"`下所有的文字内容，即
```
1
12 bcd
123
1234
```
可通过xpath的string()函数实现
```python
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
c = b.xpath('string(//ul)')
print(c)
```
```python
        1
        12bcd
        123
        1234
```
结果如上（没有去掉空白字符）,如果想要获取`ul class="2"`下所有的文字内容,可通过如下3种方式：
```python
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
# c = b.xpath('string(//ul[2])')
# c = b.xpath('string(//ul[@class="2"])')
c = b.xpath('//ul')[1].xpath('string(.)')
print(c)
```
1. 直接选取`ul`的第二个`children`
```python
c = b.xpath('string(//ul[2])')
```
2. 通过`class`属性定位
```python
c = b.xpath('string(//ul[@class="2"])')
```
3. 先获取储存所有`ul`的列表，再从列表中获取第二个`ul`,`.`表示当前节点
```python
b.xpath('//ul')[1].xpath('string(.)')
```

##### xpath中text()和string()以及data()的区别
> [XPath中的text()和string()区别](https://blog.csdn.net/weixin_39285616/article/details/78463091)

名称| 定义 | 用法
:- | :- | :-
text() | node test | 仅仅返回所指元素的文本内容
string() | 函数 | 返回所指元素的所有节点文本内容，这些文本讲会被拼接成一个字符串
data() | 函数（可保留数据类型） | 和string()函数通用,不建议经常使用，会影响XPath的性能