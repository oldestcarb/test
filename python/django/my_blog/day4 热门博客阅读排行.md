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