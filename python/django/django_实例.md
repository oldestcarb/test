models.py
```python
from django.db import models



class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()

    def __str__(self):
        return str(self.pk)


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey(BookInfo, related_name='heroinfo')

    def __str__(self):
        return str(self.pk)
```
python manage.py shell
```python
from booktest.models import BookInfo, HeroInfo

b = BookInfo()
b.btitle="射雕英雄传"
b.bpub_date=datetime(year=1990,month=1,day=10)
b.save()
h.heroinfo.create(hname=u'黄蓉',hgender=False,hcontent=u'打狗棍法')
```