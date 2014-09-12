# Create your views here.
from django.shortcuts import render_to_response
from dmWeibo.models import Photo
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def showpics(request):
	photos = Photo.objects.filter(is_show=1).filter(status=1)
	return render_to_response('showpics.html',{'photos':photos}) 

def review(request):
	photos = Photo.objects.all()[0:10]
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
	return HttpResponseRedirect(reverse('mirror.views.review'))

def remove(request,photoId):
	photo = Photo.objects.get(id=photoId)
	photo.delete()
	return HttpResponseRedirect(reverse('mirror.views.review'))