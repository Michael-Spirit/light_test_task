# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel


class Message(MPTTModel):
    author = models.ForeignKey(User, verbose_name=_('Messages author'))
    text = models.TextField(verbose_name=_('Messages text'))
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children', db_index=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<Message(id: {self.id}, " \
               f"author: {self.author}, " \
               f"time: {self.time}, " \
               f"parent: {self.parent}, " \
               f"text: {self.text})>"

    class MPTTMeta:
        order_insertion_by = ['time']
