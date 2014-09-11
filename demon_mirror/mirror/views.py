# Create your views here.
from django.shortcuts import render_to_response
from dmWeibo.models import Photo

def showpics(request):
	photos = Photo.objects.all()
	return render_to_response('showpics.html',{'photos':photos}) 