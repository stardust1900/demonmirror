# Create your views here.
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
def test(request):
	user=User()
	user.username='shawn'
	user.email='shawn@shawn.com'
	user.set_password('shawn')
	user.save()
	return HttpResponse("test")