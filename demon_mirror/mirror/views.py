# Create your views here.
from django.shortcuts import render_to_response
from dmWeibo.models import Photo

def showpics(request):
	photos = Photo.objects.all()[0:10]
	return render_to_response('showpics.html',{'photos':photos}) 

def review(request):
	photos = Photo.objects.all()[0:10]
	return render_to_response('review.html',{'photos':photos}) 