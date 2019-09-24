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

5. `blog应用的models Blog`添加排序
```python
# blog/models.py

class Blog(models.Model):

    class Meta:

        ordering = ['-created_time']
```

6. 博客分页
```python
# my_blog/settings.py
# 博客分页数量
EACH_PAGE_BLOGS_NUMBER = 7


# static/blog.css
# 分页设置居中
/* 分页 */
div.paginator {
    text-align: center;
}


# blog/templates/blog_list.html
# 分页器部分内容

{# 分页 #}
<div class="paginator">
    <p>共有{{ current_page.paginator.count }}篇博客</p>
    <ul class="pagination">
        {# 上一页 #}
        {% if current_page.has_previous %}
        <li>
            <a href="?page={{current_page.previous_page_number}}" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
            </a>
        </li>
        {% endif %}

        {% for page_num in page_range %}
        {% if page_num == current_page.number %}
        <li class="active"><span>{{ page_num }}</span></li>
        {% elif page_num == '...' %}
        <li><span>{{ page_num }}</span></li>
        {% else %}
        <li><a href="?page={{page_num}}">{{ page_num }}</a></li>
        {% endif %}
        {% endfor %}

        {# 下一页 #}
        {% if current_page.has_next %}
        <li>
            <a href="?page={{current_page.next_page_number}}"" aria-label=" Next">
                <span aria-hidden="true">&raquo;</span>
            </a>
        </li>
        {% endif %}
    </ul>
</div>



# blog/views.py
# 编写get_blog_common_date，返回博客的一些通用信息

from django.shortcuts import render
from .models import Blog, BlogType
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


def get_blog_common_date(request, object_list):
    """返回博客的一些通用信息

    :param request: request
    :param object_list: object列表
    :return: context
    """
    # 获取页码，没有则默认1
    page = request.GET.get('page', 1)

    # 获取分页器，每页7篇博客
    paginator = Paginator(object_list, 7)
    # 当前页对象
    current_page = paginator.get_page(page)
    # 当前页码数
    current_page_num = current_page.number
    # 获取页码列表，前二后二
    page_range = list(range(max(current_page_num-2, 1), current_page_num)) + list(range(current_page_num, min(current_page_num+3, paginator.num_pages+1)))

    # 如果当前页大于第3页，显示第一页
    if current_page_num-2 >1:
        page_range.insert(0, '...')
        page_range.insert(0, 1)

    # 如果当前页小于倒数第3页，显示最后一页
    if current_page_num+2<paginator.num_pages:
        page_range.append('...')
        page_range.append(paginator.num_pages)

    # 所有博客分类
    blog_types = BlogType.objects.all()

    context = {
        'blog_types': blog_types,
        'page_range': page_range,
        'current_page': current_page,
    }

    return context

def blog_list(request):
    """展示所有博客列表

    :param request: request
    :return:
    """
    # 获取所有博客
    blogs = Blog.objects.all()
    context = get_blog_common_date(request, blogs)
    return render(request, 'blog/blog_list.html', context=context)

def blog_with_type(request, blog_with_type_id):
    """展示通过博客标签分类的博客列表

    :param request: request
    :param blog_with_type_id: 博客标签ID
    :return:
    """
    # 当前博客分类
    blog_type = get_object_or_404(BlogType, id=blog_with_type_id)
    # 当前博客分类的所有博客
    blogs_with_type = Blog.objects.filter(blog_type=blog_type)

    context = get_blog_common_date(request, blogs_with_type)

    # 所有博客分类
    blog_types = BlogType.objects.all()

    context['blog_types'] = blog_types
    context['blog_type'] = blog_type

    return render(request, 'blog/blog_with_type.html', context=context)

def blog_detail(request, blog_id):
    """展示博客详细信息

    :param request: request
    :param blog_id: 博客ID
    :return:
    """
    # 通过id获取博客对象
    blog = get_object_or_404(Blog, id=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_detail.html', context=context)
```

