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

