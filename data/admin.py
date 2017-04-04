from django.contrib import admin

from data.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
