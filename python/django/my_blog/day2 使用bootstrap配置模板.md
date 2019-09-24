1. 使用bootstrap-3.3.7配置模板
> [Bootstrap](https://www.bootcss.com)
> [jquery@1.12.4](https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js)
```python
# /my_blog/settings.py
# 添加静态文件路径

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# /templates/base.html
# 全局继承模板，添加导航栏设置，引入css,js(包括全局css:base.css)

# /blog/templates/blog_list.html
# 继承/templates/base.html，全部博客列表页面
# 目前内容为博客列表（博客标题、分类、发布时间、内容前导等）
# 增加侧边栏，显示当前所有博客分类、通过bootstrap的栅格系统自适应窗口大小决定是否显示侧边栏

# /blog/templates/blog_with_type.html
# 某个标签分类下的所有博客，继承/blog/templates/blog_list.html
# 内容基本与blog_list相同

# /blog/templates/blog_detail.html
# 继承/templates/base.html，博客内容展示页面
# 目前内容为博客标题、作者、发布时间、内容

# /static/base.css
# 全局css设置

# /static/blog.css
# blog页面的相关css配置
```
2. 修改视图函数
```python
# blog/views.py

from django.shortcuts import render
from .models import Blog, BlogType
from django.shortcuts import get_object_or_404


def blog_list(request):
    # 所有博客
    blogs = Blog.objects.all()
    # 所有博客分类
    blog_types = BlogType.objects.all()

    context = {
        'blogs': blogs,
        'blog_types': blog_types,
    }

    return render(request, 'blog/blog_list.html', context=context)


def blog_detail(request, blog_id):
    # 通过id获取博客对象
    blog = get_object_or_404(Blog, id=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_detail.html', context=context)

def blog_with_type(request, blog_with_type_id):
    # 当前博客分类
    blog_type = get_object_or_404(BlogType, id=blog_with_type_id)
    # 当前博客分类的所有博客
    blogs = Blog.objects.filter(blog_type=blog_type)
    # 所有博客分类
    blog_types = BlogType.objects.all()

    context = {
        'blogs': blogs,
        'blog_type': blog_type,
        'blog_types': blog_types,
    }

    return render(request, 'blog/blog_with_type.html', context=context)
```

3. 配置urls
```python
# blog/urls.py

from django.urls import path
from blog import views
app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('type/<int:blog_with_type_id>', views.blog_with_type, name='blog_with_type'),
]
```

4. 网站添加首页
```python
# my_blog/views.py(新建)
# 添加首页视图

from django.shortcuts import render


def home(request):

    return render(request, 'home.html')

# my_blog/urls.py
# 添加首页url

from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', 'blog')),
]

# /blog/templates/home.html
# 继承/templates/base.html，首页，暂无内容
```