<!--
 * @Description: 
 * @Author: oldestcrab
 * @Github: 
 * @Date: 2019-09-26 11:27:27
 * @LastEditors: oldestcrab
 * @LastEditTime: 2019-09-26 13:03:45
 -->
1. 热门博客阅读排行
```python
blog/models.py
# blog应用的models Blog增加与read_statistic应用的models ReadNumExpandMethod反向关系

from django.contrib.contenttypes.fields import GenericRelation

class Blog(models.Model, ReadNumExpandMethod):

    # 反向关联模型，产生对应关系，不会产生字段
    read_num_details = GenericRelation(ReadNumDetail)


# read_statistic/utils.py

def get_oneday_hot_blogs(content_type, date):
    """获取某一天的前7篇博客以及当天浏览量

    :param content_type: content_type
    :param date: 某一天的日期
    :return: 某一天的前7篇博客以及当天浏览量
    """
    # 获取阅读量排行前7的博客
    today_hot_blogs = ReadNumDetail.objects.filter(content_type=content_type, date=date).order_by('-read_num')[:7]
    # print(today_hot_blogs)
    return today_hot_blogs

def get_range_day_hot_blogs(days:int):
    """获取前某天范围内的热门博客

    :param days: 前几天范围内的热门阅读，前7天：7，当天：0
    :return: 前某天范围内的热门博客字典
    """
    # 前某天的日期
    date =  timezone.now().date() - datetime.timedelta(days)

    # 热门博客字典
    hot_blogs_data = Blog.objects.filter(read_num_details__date__gte=date) \
                    .values('id', 'title').annotate(read_num_detail=Sum('read_num_details__read_num')).order_by('-read_num_detail')[:7]

    return hot_blogs_data


# my_blog.views.py
# 更新首页视图

import datetime
from django.shortcuts import render
from read_statistics.utils import get_seven_days_read_data, get_range_day_hot_blogs
from django.contrib.contenttypes.models import ContentType
from blog.models import Blog
from django.core.cache import cache


def home(request):

    content_type = ContentType.objects.get_for_model(Blog)
    # 前七天的日期，以及博客阅读数量列表
    days, read_nums = get_seven_days_read_data(content_type)

    # 今天热门博客
    range_day_hot_blogs_0 = get_range_day_hot_blogs(0)
    # 昨天热门博客
    range_day_hot_blogs_1 = get_range_day_hot_blogs(1)
    # 过去一周热门博客
    range_day_hot_blogs_7 = get_range_day_hot_blogs(7)
    # 过去一个月热门博客
    range_day_hot_blogs_30 = get_range_day_hot_blogs(30)

    context = {
        'read_nums': read_nums,
        'days': days,
        'range_day_hot_blogs_0': range_day_hot_blogs_0,
        'range_day_hot_blogs_1': range_day_hot_blogs_1,
        'range_day_hot_blogs_7': range_day_hot_blogs_7,
        'range_day_hot_blogs_30': range_day_hot_blogs_30,
    }
    return render(request, 'home.html', context=context)


# templates/home.html
# 添加相关内容
<div class="hot-data">
    <h3>今日热门博客</h3>
    <ul>
        {% for blog in range_day_hot_blogs_0 %}
        <li><a href="{% url 'blog:blog_detail' blog.id %}">{{ blog.title }}({{  blog.read_num_detail }})</a></li>
        {% empty %}
        <li>暂无热门博客</li>
        {% endfor %}
    </ul>
</div>


# static/home.css
# 相关样式设置
div.hot-data {
    text-align: center;
    margin: 2em;
}
```

2. 使用数据库缓存
```python
# my_blog/settings.py

# 配置缓存
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}


# 生成缓存表
python manage.py createcachetable


# my_blog/views.py
# 一周和一月热门博客排行使用缓存

def home(request):
    # 使用缓存，过去一周热门博客
    range_day_hot_blogs_7 = cache.get('range_day_hot_blogs_7')
    if not range_day_hot_blogs_7:
        range_day_hot_blogs_7 = get_range_day_hot_blogs(7)
        cache.set('range_day_hot_blogs_7', range_day_hot_blogs_7, 3600)

    # 使用缓存，过去一个月热门博客
    range_day_hot_blogs_30 = cache.get('range_day_hot_blogs_30')
    if not range_day_hot_blogs_30:
        range_day_hot_blogs_30 = get_range_day_hot_blogs(30)
        cache.set('range_day_hot_blogs_30', range_day_hot_blogs_30, 3600)
```

3. 用户注册登录
```python
# my_blog/views.py
# 设计用户注册，登录视图

def login(request):
    """用户登录

    :param request: request
    :return:
    """
    # 如果提交方式为post,传输数据给登录表单，否则返回空表单
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        # 判断数据是否有效，有则登录，跳转到之前的页面或者首页
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))

    else:
        login_form = LoginForm()

    context = {
        'login_form': login_form,
    }
    return render(request, 'login.html', context=context)

def register(request):
    """用户注册

    :param request: request
    :return:
    """
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        # 判断数据是否有效，有则创建用户
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            password = reg_form.cleaned_data['password']
            email = reg_form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('login')

    else:
        reg_form = RegisterForm()

    context = {
        'reg_form': reg_form,
    }
    return render(request, 'register.html', context=context)


# my_blog/forms.py
# 设计用户注册，登录表单

from django import forms
from django.contrib import auth
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    """用户登录表单

    """
    username = forms.CharField(label='用户名', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'请输入用户名'}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'请输入密码'}))

    def clean(self):
        """判断数据是否有效

        :return:
        """
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            self.cleaned_data['user'] = user
        else:
            raise ValidationError('用户名或者密码错误')

        return self.cleaned_data

class RegisterForm(forms.Form):
    """用户注册表单

    """
    username = forms.CharField(label='用户名', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'请输入用户名'}))
    email = forms.EmailField(label='用户名', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'请输入邮箱'}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'请输入密码'}))
    password_again = forms.CharField(label='密码确认', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'请再次输入密码'}))

    def clean_username(self):
        """判断用户名是否有效

        :return:
        """
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('用户名已存在')
        return username

    def clean_email(self):
        """判断邮箱是否有效

        :return:
        """
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('邮箱已存在')
        return email

    def clean_password_again(self):
        """判断密码是否一致

        :return:
        """
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise ValidationError('两次密码不一致')
        return password_again


# my_blog/urls.py
# 添加urls

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),

]


# blog_detail.py
# 测试用户登录评论
    <div class="row">
        <div class="col-xs-10 col-xd-offset-1">
            <div class="comment-area">
                <h3 class="comment-area-title">提交评论</h3>
                {% if user.is_authenticated %}
                <form action="" method="POST" style="overflow: hidden">
                    {% csrf_token %}
                    <div class="form-group">
                        <label for="comment_text">{{ user.username }},欢迎评论</label>
                        <textarea id="comment_text" class="form-control" name="text" rows="4"></textarea>
                    </div>

                    <input type="hidden" name="object_id" value="{{ blog.pk }}">
                    <input type="hidden" name="content_type" value="blog">
                    <input type="submit" value="评论" class="btn btn-primary" style="float:right">
                </form>
                {% else %}
                未登录，登录之后方可评论
                <a href="{% url 'register' %}?from={{ request.get_full_path }}" class="btn btn-danger">注册</a>or
                <a href="{% url 'login' %}?from={{ request.get_full_path }}" class="btn btn-primary">登录</a>
                {% endif %}
            </div>
            <div class="comment-area">
                <h3 class="comment-area-title">评论列表</h3>
                {% for comment in comments %}
                <div>
                    {{ comment.user.username }}
                    {{ comment.comment_time|date:'Y-m-d H:n:s' }}
                    {{ comment.text }}
                </div>


                {% empty %}
                暂无评论
                <a href=""></a>
                {% endfor %}
            </div>
        </div>

    </div>


# templates/login.html
# templates/register.html
# 新建两个模板，基本一致

{% extends "base.html" %}
{% load staticfiles %}
{% block title %}
注册
{% endblock title %}

{% block content %}
<div class="container">
    <div class="row">
        <div class="col-xs-4 col-xs-offset-4">
            <div class="panel panel-default">
                <div class="panel-heading">
                    <h3 class="panel-title">注册</h3>
                </div>
                <div class="panel-body">
                    <form action="" method="POST">
                        {% csrf_token %}
                        {{ reg_form }}
                        <input type="submit" class="btn btn-primary pull-right" value="注册">
                    </form>
                </div>
            </div>

        </div>
    </div>
</div>

{% endblock content %}
```