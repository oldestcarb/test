1. 配置模板文件，使用bootstrap
```python
# templates/share_layout/base.html
# 基础模板，所有的模板都继承于此

# templates/share_layout/nav.html
# 导航栏，在bast.html中引入

# templates/share_layout/footer.html
# 底部，在bast.html中引入
```

2. 配置博客列表展示页面,美化页面
```python
# templates/blog/blog_list.html

# 添加视图
# blog/views.py

def list(request):
    blog = Blog.objects.all()
    # 获取分页器
    paginator, page = get_page(request, blog)
    context = {
        'paginator': paginator,
        'page': page,
    }
    return render(request, 'blog/blog_list.html', context=context)


# 添加url
# blog/urls.py

urlpatterns = [
    url(r'^list/$', views.list, name='list'),
]

```
3. 配置一个通用的分页器
```python
# blog/utils.py(新建)

from django.core.paginator import Paginator

def get_page(request, object_list):
    """分页器

    :param request: request
    :param object_list: 模型所有对象
    :return: 分页器，当前页数据
    """
    # 获取当前页码，没有则默认1
    current_page = request.GET.get('page', 1)

    # 10个对象1页
    paginator = Paginator(object_list, 5)
    # 当前页数据
    page = paginator.page(current_page)

    return paginator, page
```
4. 注册admin，输入一些测试数据
5. 侧边栏样式修改
6. 编写博客展示页面