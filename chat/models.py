from django.db import models
from django.conf import settings

# Create your models here.
class ChatMessage(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="messages"
    )
    channel = models.ForeignKey('workspaces.Channel', on_delete=models.CASCADE, related_name='messages')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content
