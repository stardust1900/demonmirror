# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from dmWeibo.weibo import APIClient
from dmWeibo.models import DemonMirror
from dmWeibo.models import Photo
from django.shortcuts import render_to_response
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
from django.contrib.auth.decorators import login_required
from django.utils.timezone import LocalTimezone
# Create your views here.
APP_KEY = '2920171332'  # app key
APP_SECRET = '005a5acec91c9b92ca9eb1d349acd66a'  # app secret
CALLBACK_URL = 'http://demonmirror.com/call_back'  # callback url
DM_UID = '5052773135'

# @login_required
def band(request):
    client = APIClient(
        app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    dm = DemonMirror.objects.filter(uid=DM_UID)
    if dm:
        client.set_access_token(dm[0].access_token, dm[0].expires_in)
        if not client.is_expires():
            # return HttpResponse('already band')
            robot = client.users.show.get(uid=DM_UID)
            return render_to_response('robot.html', {'robot': robot})
    url = client.get_authorize_url()
    return HttpResponseRedirect(url)


def get_mentions(request):
    client = APIClient(
        app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    dm = DemonMirror.objects.filter(uid=DM_UID)
    if dm:
        client.set_access_token(dm[0].access_token, dm[0].expires_in)
        if not client.is_expires():
            count = 100
            page = 1

            mentions = client.statuses.mentions.get(count=count, page=page)
            while mentions.total_number > 0:
                pics = []
                lpics = []
                for st in mentions.statuses:
                    # print(st)
                    retweet_by = st.user.id
                    source = 'weibo'
                    is_show = 0
                    status = 0

                    if hasattr(st, 'retweeted_status') and hasattr(st.retweeted_status, 'pic_urls'):
                        text = st.retweeted_status.text
                        idstr = st.retweeted_status.idstr
                        try:
                        	p = Photo.objects.get(idstr=idstr)
                        except ObjectDoesNotExist:
                        	p = None
                        except MultipleObjectsReturned:
                        	continue
                        if p:
                            continue
                        post_by = st.retweeted_status.user.id
                        post_name = st.retweeted_status.user.screen_name
                        post_on = datetime.strptime(
                            st.retweeted_status.created_at, '%a %b %d %H:%M:%S +0800 %Y').replace(tzinfo=LocalTimezone())
                        retweet_on = datetime.strptime(
                            st.created_at, '%a %b %d %H:%M:%S +0800 %Y').replace(tzinfo=LocalTimezone())

                        for pic in st.retweeted_status.pic_urls:
                            thumbnail_pic = pic.thumbnail_pic
                            original_pic = pic.thumbnail_pic.replace(
                                'thumbnail', 'large')
                            pics.append(thumbnail_pic)
                            lpics.append(original_pic)
                            photo = Photo(
                                text=text, idstr=idstr, post_by=post_by, post_name=post_name, post_on=post_on, thumbnail_pic=thumbnail_pic,
                                original_pic=original_pic, retweet_by=retweet_by, source=source, is_show=is_show, status=status,retweet_on=retweet_on)
                            photo.save()
                    elif hasattr(st,'pic_urls'):
                        text = st.text
                        idstr = st.idstr
                        try:
                            p = Photo.objects.get(idstr=idstr)
                        except ObjectDoesNotExist:
                            p = None
                        except MultipleObjectsReturned:
                            continue
                        if p:
                            continue
                        post_by = st.user.id
                        post_name = st.user.screen_name
                        post_on = datetime.strptime(
                            st.created_at, '%a %b %d %H:%M:%S +0800 %Y').replace(tzinfo=LocalTimezone())
                        # print('created_at: %s'%st.created_at)
                        # print(post_on)
                        retweet_on = post_on
                        for pic in st.pic_urls:
                            thumbnail_pic = pic.thumbnail_pic
                            original_pic = pic.thumbnail_pic.replace(
                                'thumbnail', 'large')
                            pics.append(thumbnail_pic)
                            lpics.append(original_pic)
                            photo = Photo(
                                text=text, idstr=idstr, post_by=post_by, post_name=post_name, post_on=post_on, thumbnail_pic=thumbnail_pic,
                                original_pic=original_pic, retweet_by=retweet_by, source=source, is_show=is_show, status=status,retweet_on=retweet_on)
                            photo.save()
                # return
                # render_to_response('picture.html',{'pics':pics,'lpics':lpics})
                page = page + 1
                mentions = client.statuses.mentions.get(count=count, page=page)
            robot = client.users.show.get(uid=DM_UID)
            return render_to_response('robot.html', {'robot': robot,'success_msg':'同步完成！'})
            # return HttpResponse("sync completed!")
    url = client.get_authorize_url()
    return HttpResponseRedirect(url)

# http://demonmirror.com/call_back?code=97f0aeffac25a739a01f657fc346bde4


def call_back(request):
    code = request.GET.get('code')
    # print(code)
    client = APIClient(
        app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    r = client.request_access_token(code)
    access_token = r.access_token  # 新浪返回的token，类似abc123xyz456
    # print(access_token)
    # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
    expires_in = r.expires_in
    # print(expires_in)
    # print(r.uid)
    # TODO: 在此可保存access token
    # print(type(r.uid))
    # print('5052773135' == r.uid)
    if DM_UID != r.uid:
        # return HttpResponseRedirect(reverse('dmWeibo.views.band'))
        return render_to_response('result.html', {'error_msg':'绑定的不是期望账户！请重新绑定！'})
    try:
        dm = DemonMirror.objects.get(uid=r.uid)
    except Exception,e:
        dm = None
        print(e)

    if dm:
        dm.access_token = access_token
        dm.expires_in = expires_in
    else:
        dm = DemonMirror(
            uid=r.uid, access_token=access_token, expires_in=expires_in)
    dm.save()
    client.set_access_token(access_token, expires_in)
    robot = client.users.show.get(uid=DM_UID)
    return render_to_response('result.html', {'success_msg':'绑定成功！'})

def cancel_auth(request):
    dm = DemonMirror.objects.get(uid=DM_UID)
    dm.delete()
    return render_to_response('robot.html')
    # return render_to_response('result.html', {'success_msg':'绑定成功！'})
