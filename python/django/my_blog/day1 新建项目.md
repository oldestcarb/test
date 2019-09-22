1. 新建项目`my_blog`
2. 添加`.gitignore`
```python
# /.gitignore

__pycache__/
*.py[cod]

# vscode 配置
.vscode

# pycharm 配置
.idea

# settings 配置
/.env

#django 数据库迁移文件
migrations/
!migrations/__init__.py
```
3. 私密配置使用`decouple`分离
```python
# /settings.py

import os
from decouple import config, Csv

SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
```
4. 修改时区，数据库使用mysql
```python
# /settings.py

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

# 数据库设置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': config('MYSQL_HOST'),
        'PORT': config('MYSQL_PORT'),
        'USER': config('MYSQL_USER'),
        'PASSWORD': config('MYSQL_PASSWORD'),
        'NAME': config('MYSQL_DATABASE'),
    }
}
```
5. `settings.py`添加`logging`配置
```python
# /settings.py

# 日志模块logging的配置
LOGGING = {
    'version': 1,  # 指明dictConfig的版本
    'disable_existing_loggers': False,  # 表示是否禁用所有的已经存在的日志配置
    # 根日志默认日志级别
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'log_file'],
    },
    # 格式化器, 指明了最终输出中日志记录的布局
    'formatters': {
        'verbose': {
            # [时间] 日志级别 [日志对象名称.日志记录所在的函数名.日志记录所在的行号.文件名部分名称] [具体的日志信息]
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d %(module)s] %(message)s',
        }
    },
    # 过滤器, 提供了更好的粒度控制,它可以决定输出哪些日志记录。
    'filters': {
        # 判断settings的DEBUG是否开启
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 处理器,用来定义具体处理日志的方式，可以定义多种，"default"就是默认方式，"console"就是打印到控制台方式。file是写入到文件的方式，注意使用的class不同
    'handlers': {
        'log_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 与default相同
            'filename': 'my_blog.log',  # 日志输出文件
            'maxBytes': 16777216,  # 16MB
            'formatter': 'verbose'  # 制定输出的格式，注意 在上面的formatter配置里面选择一个，否则会报错
        },
        'console': {
            'level': 'DEBUG',
            # settings的DEBUG开启时才放行
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        # 将 DEBUG 以上的日志写到 /dev/null 黑洞
        'null': {
            'class': 'logging.NullHandler',
        },
        # settings的DEBUG为false时，将所有 ERROR 以上的日志邮件发送给站点管理员，当
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        # 将所有 INFO 以上的日志，发送类 console 和 mail_admins 处理其，也就是说 INFO 以上的会打印到控制台，并输入到日志文件
        'my_blog': {
            'handlers': ['log_file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        # 将所有 ERROR 以上的日志写到 mail_admins 处理器，而且不再冒泡，也就是说 django 这个 logger 不会接到 django.request 产生的日志信息
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}
```

6. 创建blog应用，添加应用，编写模型类
```python
# /blog/models.py

from django.db import models

# Create your models here.
class Author(models.Model):
    """
    博客作者类型
    """
    name = models.CharField(max_length=20, verbose_name='用户名')
    email = models.EmailField(verbose_name='邮箱')
    description = models.TextField()

    class Meta:
        verbose_name = '博客作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    博客分类
    """
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name

class Blog(models.Model):
    """
    博客
    """
    title = models.CharField(max_length=50)
    # on_delete=models.CASCADE 删除关联数据, 与之关联也删除
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    # 用于标记是否推荐博文
    recommend = models.BooleanField(default=False)

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name
        ordering = ['-publish_time']

    def __str__(self):
        return self.title

```
7. 添加静态文件配置，使用bootstrap,添加bootstrap文件到static下
```python
# /settings.py

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

8. 配置模板，测试视图函数，配置urls
```python
# /settings.py

# 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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



# /my_blog/urls.py

# 添加blog url
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'blog/', include(('blog.urls', 'blog'))),
]
```