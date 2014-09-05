# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from dmWeibo.weibo import APIClient
from dmWeibo.models import DemonMirror
from django.shortcuts import render_to_response
# Create your views here.
APP_KEY = '2920171332' # app key
APP_SECRET = '005a5acec91c9b92ca9eb1d349acd66a' # app secret
CALLBACK_URL = 'http://demonmirror.com/call_back' # callback url

def band(request):
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	dm = DemonMirror.objects.filter(uid='5052773135')
	if dm:
		client.set_access_token(dm[0].access_token,dm[0].expires_in)
		if not client.is_expires():
			return HttpResponse('already band')
	url = client.get_authorize_url()
	return HttpResponseRedirect(url)

def get_mentions(request):
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	dm = DemonMirror.objects.filter(uid='5052773135')
	if dm:
		client.set_access_token(dm[0].access_token,dm[0].expires_in)
		if not client.is_expires():
			mentions = client.statuses.mentions.get()
			pics = []
			lpics = []
			for st in mentions.statuses:
				if hasattr(st,'retweeted_status') and hasattr(st.retweeted_status,'pic_urls'):
					for pic in st.retweeted_status.pic_urls:
						pics.append(pic.thumbnail_pic)
						lpics.append(pic.thumbnail_pic.replace('thumbnail','large'))
			return render_to_response('picture.html',{'pics':pics,'lpics':lpics})
	url = client.get_authorize_url()
	return HttpResponseRedirect(url)

#http://demonmirror.com/call_back?code=97f0aeffac25a739a01f657fc346bde4
def call_back(request):
	code = request.GET.get('code')
	# print(code)
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	r = client.request_access_token(code)
	access_token = r.access_token # 新浪返回的token，类似abc123xyz456
	# print(access_token)
	expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
	# print(expires_in)
	# print(r.uid)
	# TODO: 在此可保存access token
	# print(type(r.uid))
	# print('5052773135' == r.uid)
	if '5052773135' != r.uid:
		# return HttpResponseRedirect(reverse('dmWeibo.views.band'))
		return HttpResponse("not expected user")

	dm = DemonMirror.objects.filter(uid=r.uid)
	if dm :
		dm.access_token=access_token
		dm.expires_in=expires_in
	else:
		dm = DemonMirror(uid=r.uid,access_token=access_token,expires_in=expires_in)
		dm.save()
	client.set_access_token(access_token, expires_in)
	return HttpResponse("call_back")

def cancel_auth(request):
	return HttpResponse("cancel_auth")