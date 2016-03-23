# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

# 用户类
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)


# 文章类
class Article(models.Model):
    title = models.CharField("标题", max_length=256)
    abstract = models.TextField("摘要", blank=True)
    content = models.TextField("内容")
    pub_date = models.DateTimeField("发表时间", auto_now_add=True, editable=True)
    tag = models.CharField("标签", max_length=256, blank=True)
    # update_time = models.DateTimeField("更新时间", auto_now=True, null=True)
    
    def __str__(self):
        return self.title
