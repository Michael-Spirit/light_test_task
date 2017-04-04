# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework import viewsets

from data.serializers import MessageSerializer
from data.models import Message


class MessageAPI(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.all()


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        messages = Message.objects.prefetch_related('children')

        return render(request, self.template_name, {'nodes': messages})
