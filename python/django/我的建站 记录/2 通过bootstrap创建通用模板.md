1. 修改设置，添加静态文件夹以及模板文件夹
```python
# my_blog/settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = '/static/'
```

2. 配置基础模板,下载需要的静态文件
> [bootstrap](https://v3.bootcss.com/getting-started/)
```python
# 官网下载
# static/bootstrap-3.3.7/js/bootstrap.min.js
# static/bootstrap-3.3.7/css/bootstrap.min.css
# static/bootstrap-3.3.7/css/bootstrap.min.css.map
# static/bootstrap-3.3.7/fonts/
# static/jquery-1.12.4.min.js

# templates/share_layout/base.html
添加导航栏，底部
```

3. 首页，继承于`base.html`

4. 全部博客页面
```python
# my_blog/urls.py 添加博客应用urls.py
path('blog/', include('blog.urls', namespace='blog')),

# blog/views.py 博客列表视图
blog_list()

# blog/urls.py 博客列表链接
path('', views.blog_list, name='blog_list'),

# templates/blog/blog_list.html 博客列表模板
```

5. 创建通用的分页器
> [Pagination](https://docs.djangoproject.com/en/2.2/topics/pagination/)

```python

```