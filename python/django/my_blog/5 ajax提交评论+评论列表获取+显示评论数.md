<!--
 * @Description: 
 * @Author: oldestcrab
 * @Github: 
 * @Date: 2019-09-27 11:07:39
 * @LastEditors: oldestcrab
 * @LastEditTime: 2019-09-27 13:44:16
 -->
1.评论回复功能
```python
# comment/models.py
# 评论模型设计

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import  User

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField(verbose_name='评论内容')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='用户')
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')


# comment/views.py
# 评论更新视图

from django.shortcuts import render, reverse, redirect
from .forms import CommentForm
from .models import Comment

def update_comment(request):
    # 获取跳转之前的url
    refer = request.META.get('HTTP_REFERER', reverse('home'))
    comment_form = CommentForm(request.POST, user=request.user)
    # 数据没问题则保存
    if comment_form.is_valid():
        comment = Comment()
        comment.content_object = comment_form.cleaned_data['content_object']
        comment.text = comment_form.cleaned_data['text']
        comment.user = request.user
        comment.save()

    return redirect(refer)


# comment/forms.py
# 评论表单

from django import forms
from .models import Comment
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db.models import ObjectDoesNotExist
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput())
    object_id = forms.IntegerField(widget=forms.HiddenInput())
    text = forms.CharField(label=False, widget=CKEditorWidget(config_name='comment_ckeditor'))

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(CommentForm, self).__init__(*args, **kwargs)

    def clean(self):
        # 评论对象验证
        content_type = self.cleaned_data['content_type']
        object_id = self.cleaned_data['object_id']
        try:
            # 判断是否存在模型对象
            model_class = ContentType.objects.get(model=content_type).model_class()
            # 模型对象获取数据
            model_obj = model_class.objects.get(pk=object_id)

            self.cleaned_data['content_object'] = model_obj
        except ObjectDoesNotExist:
            raise ValidationError('评论对象不存在')

        # 判断用户是否存在
        if not self.user.is_authenticated:
            raise ValidationError('用户信息不存在')

        return self.cleaned_data


# comment/urls.py
# 添加url

from django.urls import path
from . import views


urlpatterns =[
    path('update_comment', views.update_comment, name='update_comment'),
]


# blog/views.py
# 博客详情页添加评论表单实例化
def blog_detail(request, blog_id):
    context = {
        # 评论表单实例化
        'comment_form': CommentForm(initial={'object_id':blog.pk, 'content_type': ContentType.objects.get_for_model(blog).model})
    }


# my_blog/settings.py
# 添加评论回复框富文本编辑器设置

CKEDITOR_CONFIGS = {
    'default':{},
    'comment_ckeditor':{
        # 工具栏样式
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ['TextColor', 'BGcolor', 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ['Smiley', 'specialChar', 'Blockquote'],
        ],
        'width': 'auto',
        'height': '180',
        'tabSpaces': 4,
        'removePlugins': 'elementspath',
        'resize_enabled': False,
    }
}


# blog/templates/blog_detail.html
# 添加评论回复框富文本编辑器内容

{% block header_extends %}
<link rel="stylesheet" href="{% static 'blog.css' %}">
<script type="text/javascript" src="{% static "ckeditor/ckeditor-init.js" %}"></script>
<script type="text/javascript" src="{% static "ckeditor/ckeditor/ckeditor.js" %}"></script>
{% endblock header_extends %}

<div class="comment-area">
    <h3 class="comment-area-title">提交评论</h3>
    {% if user.is_authenticated %}
    <form id="comment_form" action="{% url 'comment:update_comment' %}" method="POST" style="overflow: hidden">
        {% csrf_token %}
        <label for="comment_text">{{ user.username }},欢迎评论</label>
        {{ comment_form }}
        <input type="submit" value="评论" class="btn btn-primary" style="float:right">
    </form>
    {% else %}
    未登录，登录之后方可评论
    <a href="{% url 'register' %}?from={{ request.get_full_path }}" class="btn btn-danger">注册</a>or
    <a href="{% url 'login' %}?from={{ request.get_full_path }}" class="btn btn-primary">登录</a>
    {% endif %}
</div>


# static/blog.css
/* 评论区样式设置 */
div.comment-area {
    margin-top: 2em;
}

h3.comment-area-title {
    border-bottom: 1px solid #ccc;
    padding-bottom: 0.4em;
}

div.django-ckeditor-widget {
    width: 100%;
}
```

2. ajax提交评论
```python
# templates/bast.html
# 添加扩展块{% block script_extends %}

    {% block content %}{% endblock content %}

    <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
    <script src="{% static 'jquery-1.12.4.min.js' %}"></script>
    <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
    <script src="{% static 'bootstrap-3.3.7/js/bootstrap.min.js' %}"></script>
    {% block script_extends %}{% endblock script_extends %}
</body>


# comment/views.py
# 修改update_comment 返回JsonResponse

def update_comment(request):
    comment_form = CommentForm(request.POST, user=request.user)
    # 数据没问题则保存
    if comment_form.is_valid():
        comment = Comment()
        comment.content_object = comment_form.cleaned_data['content_object']
        comment.text = comment_form.cleaned_data['text']
        comment.user = request.user
        comment.save()

        data = {
            'username':comment.user.username,
            'comment_time':comment.comment_time.strftime('%Y-%m-%d %H:%M:%S'),
            'comment_text':comment.text,
            'status':'SUCCESS',
        }

    else:
        data = {
            'status': 'ERROR',
            'message': list(comment_form.errors.values())[0][0]
        }

    return JsonResponse(data)


# blog/templates/blog_detail.html
# 修改内容
{% extends "base.html" %}
{% block title %}
{{ blog.title }}
{% endblock title %}
{% load staticfiles %}
{% block header_extends %}
<link rel="stylesheet" href="{% static 'blog.css' %}">
<script type="text/javascript" src="{% static "ckeditor/ckeditor-init.js" %}"></script>
<script type="text/javascript" src="{% static "ckeditor/ckeditor/ckeditor.js" %}"></script>
{% endblock header_extends %}
{% block nav_blog_active %}
active
{% endblock nav_blog_active %}

{% block content %}
<div class="container">
    <div class="row">
        <div class="col-xs-10 col-xd-offset-1">
            <h3>{{ blog.title }}</h3>
            <ul class="blog-info-description">
                <li>作者：{{ blog.author}}</li>
                <li>分类：<a href="{% url 'blog:blogs_with_type' blog.blog_type.id %}">{{ blog.blog_type }}</a></li>
                <li>发表日期：{{ blog.created_time|date:'Y-m-d H:i:s'}}</li>
                <li>阅读量：{{ blog.get_read_num}}</li>
            </ul>
            <div class="blog-content">{{ blog.content|safe }}</div>
            <div class="blog-more">
                <P>上一篇：
                    {# 上一篇 #}
                    {% if previous_blog  %}
                    <a href="{% url 'blog:blog_detail' previous_blog.id %}">{{ previous_blog.title }}</a>
                    {% else %}
                    这是最早的一篇文章哦
                    {% endif %}
                </p>
                <P>下一篇：
                    {# 下一篇 #}
                    {% if next_blog  %}
                    <a href="{% url 'blog:blog_detail' next_blog.id %}">{{ next_blog.title }}</a>
                    {% else %}
                    已经是最新一篇了哦
                    {% endif %}
                </p>
            </div>
        </div>
    </div>

    <div class="row">
        <div class="col-xs-10 col-xd-offset-1">
            <div class="comment-area">
                <h3 class="comment-area-title">提交评论</h3>
                {% if user.is_authenticated %}
                <form id="comment_form" action="{% url 'comment:update_comment' %}" method="POST"
                    style="overflow: hidden">
                    {% csrf_token %}
                    <label for="comment_text">{{ user.username }},欢迎评论</label>
                    {{ comment_form }}
                    <span id="comment_error" class="text-danger pull-left"></span>
                    <input type="submit" value="评论" class="btn btn-primary pull-right">
                </form>
                {% else %}
                未登录，登录之后方可评论
                <a href="{% url 'register' %}?from={{ request.get_full_path }}" class="btn btn-danger">注册</a>or
                <a href="{% url 'login' %}?from={{ request.get_full_path }}" class="btn btn-primary">登录</a>
                {% endif %}
            </div>
            <div class="comment-area">
                <h3 class="comment-area-title">评论列表</h3>
                <div id="comment_list">
                    {% for comment in comments %}
                    <div>
                        {{ comment.user.username }}
                        {{ comment.comment_time|date:'Y-m-d H:i:s' }}
                        {{ comment.text|safe }}
                    </div>

                    {% empty %}
                    <span id="no_comment">暂无评论</span>
                    <a href=""></a>
                    {% endfor %}
                </div>

            </div>
        </div>

    </div>

</div>
{% endblock content %}

{% block script_extends %}
<script type="text/javascript">
    $('#comment_form').submit(function () {
        // 清空错误信息
        $('#comment_error').text('')
        // 判断评论框是否为空
        if (CKEDITOR.instances['id_text'].document.getBody().getText().trim() == '') {
            $('#comment_error').text('评论内容不能为空');
            return false;
        }
        // 更新数据到textarea
        CKEDITOR.instances['id_text'].updateElement();
        // 异步提交
        $.ajax({
            url: "{% url 'comment:update_comment' %}",
            type: 'POST',
            cache: false,
            data: $(this).serialize(),
            success: function (data) {
                // 插入數據
                if (data['status'] == 'SUCCESS') {
                    $('#comment_list').prepend('<div>' + data['username'] + ' (' + data[
                        'comment_time'] + ') ' + data['comment_text'] + '</div>');
                    // 清空评论框
                    CKEDITOR.instances['id_text'].setData('')
                } else {
                    // 显示错误信息
                    $('#comment_error').text('评论信息不能为空')
                }
            },
            error: function (data) {
                console.log(data);
            },
        });
        return false;

    })
</script>
{% endblock script_extends %}
```

3. 评论列表获取以及评论数显示
    1. 修改所有模型的外键关联关系为
```python
#  1. 修改所有模型的外键关联关系
on_delete=models.CASCADE



# 2. 通过tempatetags的方式返回每篇博客的评论内容，以及初始化评论表单，获取每篇博客的评论数
# comment/templatetags/comment_tags.py

from ..models import Comment
from django import template
from django.contrib.contenttypes.models import ContentType
from ..models import Comment
from ..forms import CommentForm

register = template.Library()

@register.simple_tag
def get_comment_count(obj):
    """获取具体的某个模型对象的评论数

    :param obj: 具体的某个模型对象
    :return: 具体的某个模型对象的评论数
    """
    content_type = ContentType.objects.get_for_model(obj)
    return Comment.objects.filter(content_type=content_type, object_id=obj.id).count()

@register.simple_tag
def get_comment_form(obj):
    """获取评论初始表单

    :param obj: 具体的某个模型对象
    :return: 评论初始表单
    """
    content_type = ContentType.objects.get_for_model(obj).model
    form = CommentForm(initial={
        'content_type': content_type,
        'object_id': obj.id,
        'reply_comment_id': 0,
    })
    return form

@register.simple_tag
def get_comments_list(obj):
    """获取评论列表

    :param obj: 具体的某个模型对象
    :return: 评论列表
    """
    content_type = ContentType.objects.get_for_model(obj)
    # 获取评论列表
    comments = Comment.objects.filter(content_type=content_type, object_id=obj.pk, parent=None)
    return comments.order_by('-comment_time')



# 3. 添加自定义tag
# my_blog/settings.py

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
        'libraries': {
            'comment_tags': 'comment.templatetags.comment_tags',

            }

        },
    },
]

# 4. 评论框样式修改
# static/blog.css

# 5. 前端页面展示，js方法设置添加新评论
# blog/templates/blog_detail.html
```