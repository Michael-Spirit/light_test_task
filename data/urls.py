# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import routers

from data.views import MessageAPI

router = routers.DefaultRouter()
router.register(r'messages', MessageAPI, 'message')

urlpatterns = router.urls
