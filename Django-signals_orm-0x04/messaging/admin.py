# messaging/admin.py

from django.contrib import admin
from .models import Message, Notification

admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(MessageHistory)
