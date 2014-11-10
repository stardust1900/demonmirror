# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from dmWeibo.models import Photo
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from datetime import datetime
from django.utils.timezone import utc
from django.views.decorators.csrf import csrf_exempt

def showpics(request):
	photos = Photo.objects.filter(is_show=1).filter(status=1).order_by('pass_on')
	return render_to_response('showpics.html', {'photos': photos})

@login_required
def review(request):
	limit = 20  # 每页显示的记录数
	photos = Photo.objects.all().order_by('-retweet_on')
	paginator = Paginator(photos, limit)  # 实例化一个分页对象
	page = request.GET.get('page')  # 获取页码
	try:
		photos = paginator.page(page)  # 获取某页对应的记录
	except PageNotAnInteger:  # 如果页码不是个整数
		photos = paginator.page(1)  # 取第一页的记录
	except EmptyPage:  # 如果页码太大，没有相应的记录
		photos = paginator.page(paginator.num_pages)  # 取最后一页的记录

	return render_to_response('review.html',{'photos':photos}) 

@login_required
def display(request,photoId):
	photo = Photo.objects.get(id=photoId)
	if 0==photo.is_show:
		photo.is_show = 1
	else:
		photo.is_show = 0
	photo.save()
	return HttpResponseRedirect(reverse('mirror.views.review'))
@login_required
def approve(request,photoId):
	Photo.objects.filter(id=photoId).update(status = 1,is_show = 1,pass_on=datetime.utcnow().replace(tzinfo=utc))
	# photo.status = 1
	# photo.is_show = 1
	# photo.pass_on = datetime.utcnow().replace(tzinfo=utc)
	# print(photo.pass_on)
	# photo.save()
	return HttpResponseRedirect(reverse('mirror.views.review')+'?page='+request.GET.get('page'))
@login_required
def remove(request,photoId):
	photo = Photo.objects.get(id=photoId)
	photo.delete()
	return HttpResponse("success")
@login_required
@csrf_exempt
def addTag(request):
	# print(request)
	if request.method == 'POST':
		photoId = request.POST.get('photoId','');
		tag = request.POST.get('tag','');
		# print(photoId)
		# print(tag)
		if ("" != photoId and "" != tag):
			photo = Photo.objects.get(id=photoId)
			print(photo.tags)
			if photo.tags.count(tag) == 0:
				photo.tags.append(tag);
				photo.save()
				return HttpResponse(tag)
			else:
				return HttpResponse("")
	return HttpResponse("error")
@login_required
@csrf_exempt
def removeTag(request):
	if request.method == 'POST':
		photoId = request.POST.get('photoId','');
		tag = request.POST.get('tag','');
		if ("" != photoId and "" != tag):
			photo = Photo.objects.get(id=photoId)
			photo.tags.remove(tag)
			photo.save()
			ret = ""
			for tag in photo.tags:
				ret = ret +tag+","
			if "" != ret:
				ret=ret[:-1]
			return HttpResponse(ret)
	return HttpResponse("error")
