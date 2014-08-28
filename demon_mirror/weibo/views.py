# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from weibo import APIClient
# Create your views here.
APP_KEY = '2920171332' # app key
APP_SECRET = '005a5acec91c9b92ca9eb1d349acd66a' # app secret
CALLBACK_URL = 'http://demonmirror.com/call_back' # callback url

def band(request):
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	url = client.get_authorize_url()
	return HttpResponseRedirect(url)

#http://demonmirror.com/call_back?code=97f0aeffac25a739a01f657fc346bde4
def call_back(request):
	code = request.GET.get('code')
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	r = client.request_access_token(code)
	access_token = r.access_token # 新浪返回的token，类似abc123xyz456
	expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
	# TODO: 在此可保存access token
	client.set_access_token(access_token, expires_in)
	return HttpResponse("call_back")

def cancel_auth(request):
	return HttpResponse("cancel_auth")