1. 博客按月分类
```python
# static/base.css

/* 设置全局ul样式 */
ul {
    list-style-type: none!important;
}

# blog/templates/blog_with_date.html(新建, 基本和blog_with_type.html一样)
# blog/templates/blog_list.html

{# 按月分类 #}
<div class="panel panel-default">
    <div class="panel-heading">日期归档</div>
    <div class="panel-body">
        <ul class="blog-dates">
            {% for blog_date in blog_dates %}
            <li>
                <a href="{% url 'blog:blogs_with_date' blog_date.year blog_date.month %}">
                    {{ blog_date|date:'Y-m' }}
                </a>
            </li>
            {% empty %}
            <li>暂无分类</li>
            {% endfor %}
        </ul>
    </div>
</div>


# blog/urls.py
# 按月分类url

urlpatterns = [
    path('date/<int:year>/<int:month>', views.blogs_with_date, name='blogs_with_date'),
]


# blog/views.py
# 增加视图blogs_with_date,修改get_blog_list_common_date

def get_blog_list_common_date(request, object_list):
    """返回博客的一些通用信息

    :param request: request
    :param object_list: object列表
    :return: context
    """
    # 获取页码，没有则默认1
    page = request.GET.get('page', 1)

    # 获取分页器，每页7篇博客
    paginator = Paginator(object_list, settings.EACH_PAGE_BLOGS_NUMBER)
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

    # 按月分类
    blog_dates = Blog.objects.dates('created_time', 'month', 'DESC')

    context = {
        'blog_types': blog_types,
        'page_range': page_range,
        'current_page': current_page,
        'blog_dates': blog_dates,
    }

    return context

def blogs_with_date(request, year, month):

    # 当前日期的所有博客
    blogs_with_date = Blog.objects.filter(created_time__year=year, created_time__month=month)

    context = get_blog_list_common_date(request, blogs_with_date)

    context['blogs_with_date'] = blogs_with_date
    context['current_date'] = str(year) + '-' + str(month)

    return render(request, 'blog/blog_with_type.html', context=context)
```
2. 显示分类统计的数量
```python
# blog/views.py
# 修改分类获取，添加数量统计

def get_blog_list_common_date(request, object_list):
    """返回博客的一些通用信息

    :param request: request
    :param object_list: object列表
    :return: context
    """
    # 获取页码，没有则默认1
    page = request.GET.get('page', 1)

    # 获取分页器，每页7篇博客
    paginator = Paginator(object_list, settings.EACH_PAGE_BLOGS_NUMBER)
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

    # 按月分类, 以及数量统计
    blog_dates_dict = {}
    for blog in Blog.objects.dates('created_time', 'month', 'DESC'):
        blog_count = Blog.objects.filter(created_time__year=blog.year, created_time__month=blog.month).count()
        blog_dates_dict[blog] = blog_count

    # 所有博客分类, 以及数量统计
    blog_types_count = BlogType.objects.annotate(blog_count=Count('blog'))

    context = {
        'blog_types': blog_types_count,
        'page_range': page_range,
        'current_page': current_page,
        'blog_dates_dict': blog_dates_dict,
    }

    return context


# blog/templates/blog_list.html
# 修改显示效果，添加数量统计

<ul class="blog-dates">
   {% for blog_date, blog_count in blog_dates_dict.items %}
   <li>
       <a href="{% url 'blog:blogs_with_date' blog_date.year blog_date.month %}">
           {{ blog_date|date:'Y-m' }}({{ blog_count }})
       </a>
   </li>
   {% empty %}
   <li>暂无分类</li>
   {% endfor %}
</ul>
```

3. 后台富文本编辑
```python
pip install django-ckeditor
pip install pillow
# my_blog/settings.py

# 注册应用
INSTALLED_APPS = [
    'blog',
    'ckeditor',
    'ckeditor_uploader',
]

# 设置media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 配置ckeditor
CKEDITOR_UPLOAD_PATH = 'upload/'


# my_blog/urls.py
# 配置相关url

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('blog/', include('blog.urls', 'blog')),
]

# 设置上传的图片路径
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# blog/models.py
# 修改模型

from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
    content = RichTextUploadingField(verbose_name='内容')
```

4. 阅读数量统计
```python
# blog/models.py
# 增加阅读数字段

class Blog(models.Model):
    read_num = models.IntegerField(default=0, verbose_name='阅读量')


# blog/admin.py
# 后台显示阅读数字段

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'read_num', 'blog_type', 'created_time', 'last_update_time', 'is_delete')


# blog/views.py
# 通过cookies判断是否阅读过

def blog_detail(request, blog_id):
    """展示博客详细信息

    :param request: request
    :param blog_id: 博客ID
    :return:
    """
    # 通过id获取博客对象
    blog = get_object_or_404(Blog, id=blog_id)
    if not request.COOKIES.get(f'blog_{blog_id}_read'):
        blog.read_num += 1
        blog.save()

    # 上一条博客
    previous_blog = Blog.objects.filter(created_time__lt=blog.created_time).first()

    # 下一条博客
    next_blog = Blog.objects.filter(created_time__gt=blog.created_time).last()

    context = {
        'blog': blog,
        'previous_blog': previous_blog,
        'next_blog': next_blog,
    }

    response = render(request, 'blog/blog_detail.html', context=context)
    response.set_cookie(f'blog_{blog_id}_read', 'true')

    return response

# 修改模板
# blog/templates/blog_list.html
# blog/templates/blog_detail.html
```