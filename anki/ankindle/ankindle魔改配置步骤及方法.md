## anki + kidle

### 参考
> [Anki+Kindle=AnKindle：生词导入从未如此轻松](https://zhuanlan.zhihu.com/p/35163164)  
> [Anki插件AnKindle视频教程及配套模板](http://www.laohuang.net/20180429/ankindle_template/)


### 步骤
1. 安装`anikindle`(参考链接有详细教程，不再赘述)
    > 代码**1016931132**
    >ankindle基本使用步骤如下：
    ```
    1.（必选）选择Kindle数据库 
    保证Kindle USB接入电脑，插件在Windows上是自动识别Kindle单词数据库，其他系统第一次需要   手动选择。 

    2. （必选）导入语言类型 

    对于用Kindle的多语言学习者，单词本里可能包含不止一种语言，这个下拉框用于选择您需要导入的    语言生词。 

    3.（必选）保存为笔记类型 

    选择Kindle单词导出的目标笔记类型，本插件默认提供一个类型为【AnKindle】， 您可以在Anki菜 单中的【工具】>【笔记类型管理】中查看其具体内容。

    4.（必选）保存到记忆库 

    选择Kindle单词的目标保存记忆库。 

    5.（可选）MDX词典 

    模板提供一个字段为【mdx_dict】您可以选择自己喜欢的MDX字典，插件如果此选项被提供，那么插 件会查询这个 词典然后把可用的查询内容放进【mdx_dict】 

    6.（可选）仅新词

    如果勾选，插件不会导入被Kindle标记为【已掌握】的单词。

    7.（可选）生词预览（单词管理）

    提供生词以及已掌握的单词预览，和一些简单更新Kindle数据库操作。

    8. 一键导入

    ```

2. 导入同一目录下的`AnKindle-Vocab.apkg`模板，修改配置 
    >- 同一目录下的`ankidle.js`为`ankindle-vocab`的卡片设计，正面、通用、背面都在里面，分别复制过去就行。
    >- 同一目录下的`_collins_c.css`为mdx词典`collins`的样式设计，放到媒体库中，方法如下： \
     打开anki-工具-插件-打开插件文件夹-在打开的文件夹选择上一个文件夹（一般为`anki+版本号`）-选择当前用户名字的文件夹打开-选择collection.media-复制到这个文件夹中 
3. 插入kindle，`ctrl+k`导入生词（参考链接有详细教程，不再赘述）

### 完成之后的效果图如下：
- #### 正面
![ankindle-vocab模板正面效果_2018-05-26_22-36-39](http://ww1.sinaimg.cn/large/e2528559gy1frp4d8mxf1j20i40ieaaa.jpg)

- #### 背面
![ankindle-vocab模板背面效果_2018-05-26_22-37-41](http://ww1.sinaimg.cn/large/e2528559gy1frp4f7bbodj20i40rn0tr.jpg)