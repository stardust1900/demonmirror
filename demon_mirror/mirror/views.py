# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from dmWeibo.models import Photo
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


def showpics(request):
	photos = Photo.objects.filter(is_show=1).filter(status=1)
	return render_to_response('showpics.html', {'photos': photos})


def review(request):
	limit = 20  # 每页显示的记录数
	photos = Photo.objects.all().order_by('-created_on')
	paginator = Paginator(photos, limit)  # 实例化一个分页对象
	page = request.GET.get('page')  # 获取页码
	try:
		photos = paginator.page(page)  # 获取某页对应的记录
	except PageNotAnInteger:  # 如果页码不是个整数
		photos = paginator.page(1)  # 取第一页的记录
	except EmptyPage:  # 如果页码太大，没有相应的记录
		photos = paginator.page(paginator.num_pages)  # 取最后一页的记录

	return render_to_response('review.html',{'photos':photos}) 

def display(request,photoId):
	photo = Photo.objects.get(id=photoId)
	if 0==photo.is_show:
		photo.is_show = 1
	else:
		photo.is_show = 0
	photo.save()
	return HttpResponseRedirect(reverse('mirror.views.review'))

def approve(request,photoId):
	photo = Photo.objects.get(id=photoId)
	photo.status = 1
	photo.is_show = 1
	photo.save()
	return HttpResponseRedirect(reverse('mirror.views.review')+'?page='+request.GET.get('page'))

def remove(request,photoId):
	photo = Photo.objects.get(id=photoId)
	photo.delete()
	return HttpResponse("success")
