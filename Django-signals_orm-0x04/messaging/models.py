# messaging/models.py

from django.db import models
from django.contrib.auth.models import User
from .managers import UnreadMessagesManager  # ✅ Import the custom manager

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    parent_message = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    objects = models.Manager()  # Default manager
    unread = UnreadMessagesManager()  # ✅ Attach custom manager

    def __str__(self):
        return f"From {self.sender} to {self.receiver}: {self.content[:20]}"
