# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view

from data.views import IndexView
from accounts.views import LoginView

schema_view = get_swagger_view(title='swagger')

prefix = r'^api/'

urlpatterns = [
    url(r'^docs/', schema_view, name='swagger'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),

    url(prefix, include([
        url(r'^accounts/', include("accounts.urls", namespace="accounts")),
        url(r'^data/', include("data.urls", namespace='data')),
    ])),
]
