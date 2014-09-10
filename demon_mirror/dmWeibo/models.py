# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class DemonMirror(models.Model):
	uid = models.CharField(max_length=140,primary_key=True)
	access_token = models.CharField(max_length=140)
	expires_in = models.CharField(max_length=140)

# 
class Photo(models.Model):
	text = models.CharField(max_length=140)
	thumbnail_pic = models.CharField(max_length=140)
	original_pic = models.CharField(max_length=140)
	post_by = models.CharField(max_length=140)
	retweet_by = models.CharField(max_length=140)
	source = models.CharField(max_length=140) # where this photo from weibo douban fanfou this site
	is_show = models.SmallIntegerField() #0:不展示，1：展示
	status = models.SmallIntegerField()  #0：待审核 1：审核通过  2：发布者删除
	post_on = models.DateTimeField(auto_now_add=False, null=True)  #原始发布日期
	created_on = models.DateTimeField(auto_now_add=True, null=True) #在本站的发布日期
	tags = ListField()
	comments = ListField(EmbeddedModelField('Comment'))
	marks = ListField(EmbeddedModelField('Mark'))
	mark = models.DecimalField(max_digits=4, decimal_places=1) #图片得分
	marked_num = models.IntegerField()  #评分人数

#评分对象
class Mark(models.Model):
	marker = models.CharField(max_length=140) #打分人
	mark = models.SmallIntegerField() #评分
	created_on = models.DateTimeField(auto_now_add=True, null=True)

class Comment(models.Model):
	text = models.CharField(max_length=140)
	post_by = models.CharField(max_length=140)
	created_on = models.DateTimeField(auto_now_add=True, null=True)